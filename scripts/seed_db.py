"""
Script de inicialización y datos de prueba (Seeds) para SchoolSysWeb.
Ejecutar con:
    python -m scripts.seed_db
"""
import asyncio
from datetime import date
from decimal import Decimal

from sqlalchemy import select

from app.core.database import AsyncSessionLocal, Base, engine
from app.core.security import get_password_hash
from app.models import (
    Attendance,
    AttendanceStatus,
    Grade,
    Group,
    Payment,
    PaymentMethod,
    PaymentStatus,
    Role,
    Student,
    Subject,
    User,
)


async def seed_data():
    print("🌱 Iniciando población de datos iniciales en la base de datos...")

    # 1. Asegurar que las tablas existan
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Tablas verificadas/creadas correctamente.")

    async with AsyncSessionLocal() as session:
        # 2. Roles del Sistema
        roles_data = [
            {"name": "ADMIN", "description": "Administrador con control total del sistema"},
            {"name": "TEACHER", "description": "Docente encargado de materias, asistencias y calificaciones"},
            {"name": "STUDENT", "description": "Alumno con acceso a consulta de notas y asistencias"},
            {"name": "STAFF", "description": "Personal administrativo y control de cobranza"},
        ]

        roles_dict: dict[str, Role] = {}
        for r_data in roles_data:
            stmt = select(Role).where(Role.name == r_data["name"])
            existing_role = (await session.execute(stmt)).scalars().first()
            if not existing_role:
                new_role = Role(**r_data)
                session.add(new_role)
                await session.flush()
                roles_dict[r_data["name"]] = new_role
                print(f"  + Rol creado: {r_data['name']}")
            else:
                roles_dict[r_data["name"]] = existing_role

        # 3. Usuario Administrador Inicial
        admin_email = "admin@schoolsys.com"
        admin_user = (
            (await session.execute(select(User).where(User.email == admin_email)))
            .scalars()
            .first()
        )
        if not admin_user:
            admin_user = User(
                email=admin_email,
                username="admin",
                full_name="Administrador del Sistema",
                hashed_password=get_password_hash("admin123"),
                is_active=True,
                role_id=roles_dict["ADMIN"].id,
            )
            session.add(admin_user)
            await session.flush()
            print(f"  + Usuario Admin creado: {admin_email} (Contraseña: admin123)")
        else:
            print(f"  * Usuario Admin ya existente: {admin_email}")

        # 4. Grupo de muestra
        group_stmt = select(Group).where(Group.name == "1° A", Group.school_cycle == "2026-2027")
        sample_group = (await session.execute(group_stmt)).scalars().first()
        if not sample_group:
            sample_group = Group(
                name="1° A",
                grade_level="Secundaria",
                shift="Matutino",
                school_cycle="2026-2027",
            )
            session.add(sample_group)
            await session.flush()
            print("  + Grupo creado: 1° A (Secundaria Matutino 2026-2027)")

        # 5. Materia de muestra
        subject_stmt = select(Subject).where(Subject.code == "MAT-101")
        sample_subject = (await session.execute(subject_stmt)).scalars().first()
        if not sample_subject:
            sample_subject = Subject(
                code="MAT-101",
                name="Matemáticas I",
                description="Álgebra básica y razonamiento cuantitativo",
                credits=5,
            )
            session.add(sample_subject)
            await session.flush()
            print("  + Materia creada: MAT-101 (Matemáticas I)")

        # 6. Alumno de muestra
        enrollment_num = "EST-2026-001"
        student_stmt = select(Student).where(Student.enrollment_number == enrollment_num)
        sample_student = (await session.execute(student_stmt)).scalars().first()
        if not sample_student:
            sample_student = Student(
                enrollment_number=enrollment_num,
                first_name="Juan Carlos",
                last_name="Pérez García",
                birth_date=date(2010, 5, 15),
                gender="M",
                curp_or_dni="PEGA100515HDFRRN01",
                group_id=sample_group.id if sample_group else None,
            )
            session.add(sample_student)
            await session.flush()
            print(f"  + Alumno registrado: Juan Carlos Pérez García ({enrollment_num})")

            # 7. Asistencia de muestra para el alumno
            sample_attendance = Attendance(
                student_id=sample_student.id,
                subject_id=sample_subject.id,
                date=date.today(),
                status=AttendanceStatus.PRESENT,
                remarks="Asistencia puntual al aula",
            )
            session.add(sample_attendance)
            print("  + Registro de Asistencia de muestra creado")

            # 8. Calificación de muestra para el alumno
            sample_grade = Grade(
                student_id=sample_student.id,
                subject_id=sample_subject.id,
                period="1er Trimestre",
                score=9.5,
                remarks="Excelente participación y proyectos entregados",
            )
            session.add(sample_grade)
            print("  + Registro de Calificación de muestra creado: 9.5")

            # 9. Pago de muestra para el alumno
            sample_payment = Payment(
                student_id=sample_student.id,
                concept="Inscripción Ciclo Escolar 2026-2027",
                amount=Decimal("1500.00"),
                payment_date=date.today(),
                status=PaymentStatus.PAID,
                payment_method=PaymentMethod.TRANSFER,
                receipt_number="REC-2026-0001",
            )
            session.add(sample_payment)
            print("  + Registro de Pago de muestra creado: $1,500.00 (REC-2026-0001)")

        await session.commit()
        print("\n🎉 ¡Población de datos iniciales completada con éxito!")


async def main():
    try:
        await seed_data()
    finally:
        await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())

