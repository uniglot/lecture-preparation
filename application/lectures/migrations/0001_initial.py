# Generated by Django 4.2.13 on 2024-06-03 11:13

from django.db import migrations, models
import django.db.models.deletion


def create_initial_records(apps, schema_editor):
    Department = apps.get_model("lectures", "Department")
    Person = apps.get_model("lectures", "Person")
    Professor = apps.get_model("lectures", "Professor")
    Lecture = apps.get_model("lectures", "Lecture")

    Department.objects.bulk_create([
        Department(name="컴퓨터공학과", code="CS", category="ENG"),
        Department(name="화학공학과", code="CE", category="ENG"),
        Department(name="물리학과", code="PH", category="SCI"),
        Department(name="영어영문학과", code="EL", category="LIT"),
        Department(name="불어불문학과", code="FL", category="LIT"),
        Department(name="회화과", code="PA", category="ART"),
    ])

    departments = Department.objects.all()
    people = []
    family_names = ["김", "이", "박", "최", "정", "강", "조", "윤", "장", "임", "한", "오", "서", "신", "황", "안", "송", "전", "홍"]
    given_names = [
        "민준",
        "서윤",
        "서준",
        "서연",
        "예준",
        "지우",
        "도윤",
        "하준",
        "수아",
        "지민",
        "지호",
        "지안",
        "예린",
        "지윤",
        "시우",
        "하윤",
        "주원",
        "지원",
        "윤서",
        "지후",
        "하율",
        "하빈",
        "유진",
        "지아",
        "수현",
        "은우",
        "도연",
        "연우",
        "수빈",
        "예빈",
        "시윤",
        "태윤",
        "윤아",
        "서진",
        "유나",
        "예지",
        "서현",
        "하람",
        "민서",
        "다은",
        "소윤",
        "지율",
        "다인",
        "준우",
        "서하",
        "서영",
        "민성",
        "윤호",
        "유준",
        "은서",
        "하연",
        "지웅",
        "소연",
        "다윤",
        "현우",
        "시현",
        "수호",
        "은수",
        "승우",
        "지훈",
        "시영",
        "하람",
        "예나",
        "민호",
        "유빈",
        "시완",
        "주하",
        "하은",
        "은채",
        "하온",
        "민아",
        "수아",
        "도현",
        "도영",
        "시은",
        "하린",
        "수정",
        "지수",
        "예슬",
        "하온",
        "서율",
        "다영",
        "하영",
        "도율",
        "소은",
        "채원",
        "예나",
        "준서",
        "지유",
        "채은",
        "은성",
        "시안",
        "도경",
        "은하",
        "주현",
        "연서",
        "세빈",
        "주영",
        "하늘",
        "시영",
        "채윤",
        "유나",
    ]

    count = 0
    for family_name in family_names:
        for given_name in given_names:
            people.append(Person(name=family_name+given_name, department=departments[count%6]))
            count += 1
    Person.objects.bulk_create(people)

    Professor.objects.bulk_create([
        Professor(name="Prof. Kim", email="kim@test.com", department=departments[0]),
        Professor(name="Prof. Lee", email="lee@test.com", department=departments[1]),
        Professor(name="Prof. Park", email="park@test.com", department=departments[2]),
        Professor(name="Prof. Choi", email="choi@test.com", department=departments[3]),
        Professor(name="Prof. Jeong", email="jeong@test.com", department=departments[4]),
        Professor(name="Prof. Kang", email="kang@test.com", department=departments[5]),
    ])

    professors = Professor.objects.all()
    lectures = []
    prefixes = ["기본 ", "고급 ", "현대 ", "고대 ", "중세 ", "중급 ", "실무 ", "실용 "]
    topics = ["진", "케이틀린", "애쉬", "징크스", "럭스", "타릭", "녹턴", "벡스", "소나", "케넨"]
    suffixes = ["의 이해", "의 역사", "학 개론", "학 입문", "의 응용"]

    count = 0
    for prefix in prefixes:
        for topic in topics:
            for suffix in suffixes:
                lectures.append(
                    Lecture(
                        name=prefix+topic+suffix,
                        code=topic+str(count),
                        professor=professors[count%6],
                        register_limit=30,
                    )
                )
                count += 1
    Lecture.objects.bulk_create(lectures)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('code', models.CharField(max_length=2)),
                ('category', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.department')),
                ('total_credit', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.department')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('code', models.CharField(max_length=5)),
                ('credit', models.IntegerField(default=3)),
                ('register_limit', models.IntegerField()),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.professor')),
                ('students', models.ManyToManyField(to='lectures.person')),
            ],
        ),
        migrations.RunPython(create_initial_records),
    ]