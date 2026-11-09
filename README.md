# Backend Developer Examination

ยินดีต้อนรับสู่แบบทดสอบสำหรับตำแหน่ง Backend Developer แบบทดสอบนี้ออกแบบมาเพื่อประเมินทักษะและความรู้ในการพัฒนา Backend โดยครอบคลุมตั้งแต่การเขียนโปรแกรมเชิงตรรกะ, ความเข้าใจใน Database และ API, ไปจนถึงการพัฒนา RESTful API ด้วย Framework จริง

## รายละเอียดแบบทดสอบ

แบบทดสอบถูกแบ่งออกเป็น 4 ส่วนหลัก ผู้สมัครสามารถเข้าไปดูรายละเอียดและทำแบบทดสอบในแต่ละโฟลเดอร์ได้เลย

### ส่วนที่ 1: Logic Test
การทดสอบทักษะการแก้ปัญหาและการเขียนโปรแกรมเชิงตรรกะ (Python) ประกอบด้วย 4 ข้อย่อย:
- `1_find_tailing_zero`: หาจำนวนเลข 0 ท้ายสุดของค่า factorial
- `2_index_of_max`: หา index ของค่าที่มากที่สุดใน array
- `3_number_to_thai`: แปลงตัวเลขเป็นข้อความภาษาไทย
- `4_number_to_roman`: แปลงตัวเลขเป็นเลขโรมัน

### ส่วนที่ 2: Database Concept
การทดสอบความเข้าใจหลักการทำงานของฐานข้อมูล ประกอบด้วย 2 ข้อ (ตอบคำถามลงในไฟล์ `README.md` ของแต่ละข้อย่อย):
- `1_acid_concept`: อธิบายหลักการ ACID
- `2_index_concept`: อธิบายเกี่ยวกับการทำ Index

### ส่วนที่ 3: API Concept
การทดสอบความเข้าใจในการออกแบบและทำงานของ API ประกอบด้วย 2 ข้อ (ตอบคำถามลงในไฟล์ `README.md` ของแต่ละข้อย่อย):
- `1_idempotency`: ความเข้าใจเรื่อง Idempotency
- `2_data_format`: ความเข้าใจเรื่อง Data format ของ API

### ส่วนที่ 4: REST API Development (Django)
บททดสอบการปฏิบัติงานจริง โดยใช้ Django REST Framework ในการพัฒนา API สำหรับระบบจัดการข้อมูลโรงเรียนและบุคลากร สามารถดูรายละเอียด Requirement ทั้งหมดได้ที่ `4_rest_api/api_exam.md`

---

## เกณฑ์การให้คะแนน (คะแนนเต็ม 20 คะแนน)

เพื่อให้ผู้สมัครเห็นภาพรวมของน้ำหนักคะแนนในแต่ละส่วน เราได้แบ่งคะแนนและกำหนดสัดส่วนดังนี้:

| ส่วนที่ | หัวข้อ | คะแนน | รายละเอียด |
| :--- | :--- | :---: | :--- |
| **1** | **Logic Test** | **2** | ข้อละ 0.5 คะแนน: ประเมินจากความถูกต้องของผลลัพธ์, โค้ดที่อ่านง่าย, และประสิทธิภาพ |
| **2** | **DB Concept** | **5** | ข้อละ 2.5 คะแนน: ประเมินจากความถูกต้อง, ครบถ้วน, และความเข้าใจในเหตุผลที่อธิบาย |
| **3** | **API Concept** | **5** | ข้อละ 2.5 คะแนน: ประเมินจากความถูกต้อง, ครบถ้วน, และความเข้าใจในเหตุผลที่อธิบาย |
| **4** | **REST API (Django)** | **8** | ประเมินจากความครบถ้วนของ Requirement, โครงสร้างโค้ด, การใช้งาน Serializer/Filter, และ Best Practices |
| | **รวมทั้งหมด** | **20** | |

## Run the submission

Use Python 3.12 and a virtual environment. From the repository root:

```sh
python -m pip install -r 4_rest_api/requirements.txt
python -m unittest discover -s 1_logic_test
cd 4_rest_api
python manage.py migrate
python manage.py test
python manage.py createsuperuser
python manage.py runserver
```

The four collections are `/api/v1/schools/`, `/api/v1/classrooms/`, `/api/v1/teachers/` and `/api/v1/students/`. Authenticate using HTTP Basic with the local account. Send JSON for writes. Append an ID and trailing slash to retrieve, update or delete one record. Classroom and personnel relationships use numeric IDs. Teacher counts include distinct teachers assigned to classrooms in the school.

The Roman numeral exercise accepts 1 through 3999, the conventional range for subtractive notation without overlines. A tied maximum returns its first index.
