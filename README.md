# Data Science SQL Project 2 - JOINS

## Proje Kurulumu

1. Projeyi **fork** edin ve kendi hesabınıza **clone** edin.
2. Terminal'de proje klasörüne girin.

### Mac / Linux
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Windows
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Veritabanı Kurulumu

Soruları çözebilmek için önce local PostgreSQL veritabanınızda tabloları oluşturmanız gerekiyor:

1. PostgreSQL'in bilgisayarınızda kurulu ve çalışır durumda olduğundan emin olun.
2. `scripts/init_db.py` dosyasındaki SQL komutlarını sırasıyla kendi local veritabanınızda çalıştırın.
3. Tabloların doğru oluştuğundan emin olmak için her tabloya birer `SELECT *` sorgusu atın.

> **Not:** `data/question.py` içindeki `connect_db()` fonksiyonunda veritabanı bağlantı bilgileri var.
> Localinizde test ederken kendi bilgilerinizle değiştirin.
> **Pushlarken bu bilgileri varsayılan haliyle bırakın** (CI/CD ortamında bu bilgilerle çalışıyor).

## Başlangıç Ayarları

Kodlamaya başlamadan önce şu iki dosyada kendi bilgilerinizi güncellemeniz gerekiyor:

1. **`tests/test_question.py`** — Dosyanın altındaki `run_tests()` fonksiyonunda `user_id` değerini **kendi kullanıcı ID'nizle** değiştirin.
2. **`data/question.py`** — `connect_db()` fonksiyonundaki veritabanı şifresini kendi local PostgreSQL şifrenizle değiştirin. **Pushlarken varsayılan haliyle bırakın.**

## Çalışma Şekli

- Sadece `data/question.py` dosyasında çalışın.
- Her `question_X_query()` fonksiyonu içindeki boş `cursor.execute('')` satırına SQL sorgunuzu yazın.
- Diğer dosyaları değiştirmeyin.

## Testleri Çalıştırma

```bash
python watch.py
```

Bu komut dosya değişikliklerini izler ve her kaydettiğinizde testleri otomatik çalıştırır.

Tek seferlik çalıştırmak için:
```bash
pytest tests/test_question.py -s -v
```

## Tablolar

### students
| Sütun | Tip |
|-------|-----|
| student_id | SERIAL (PK) |
| first_name | VARCHAR(50) |
| last_name | VARCHAR(50) |
| email | VARCHAR(100) |
| age | INT |

### courses
| Sütun | Tip |
|-------|-----|
| course_id | SERIAL (PK) |
| course_name | VARCHAR(100) |
| category | VARCHAR(50) |

### instructors
| Sütun | Tip |
|-------|-----|
| instructor_id | SERIAL (PK) |
| name | VARCHAR(100) |
| expertise | VARCHAR(100) |

### enrollments
| Sütun | Tip |
|-------|-----|
| enrollment_id | SERIAL (PK) |
| student_id | INT (FK -> students) |
| course_id | INT (FK -> courses) |
| enrollment_date | DATE |

### course_instructors
| Sütun | Tip |
|-------|-----|
| id | SERIAL (PK) |
| course_id | INT (FK -> courses) |
| instructor_id | INT (FK -> instructors) |

## Sorular

### Bölüm 1: WHERE Sorguları

1. **students** tablosundan yaşı **22'den büyük** öğrencileri listele. (Tüm sütunlar)

2. **courses** tablosundan kategorisi **'Veritabanı'** olan kursları getir. (Tüm sütunlar)

3. **students** tablosundan ismi **'A' harfi ile başlayan** öğrencileri bul. (Tüm sütunlar)

4. **courses** tablosundan kurs ismi içinde **'SQL' geçenleri** listele. (Tüm sütunlar)

5. **students** tablosundan yaşı **22 ile 24 arasında** (dahil) olan öğrencileri getir. (Tüm sütunlar)

### Bölüm 2: JOIN Sorguları

6. Kursa **kayıtlı olan** öğrencilerin isimlerini listele. (`first_name`, `last_name` — tekrar etmeyen, `student_id`'ye göre sıralı)

7. **Veritabanı** kategorisindeki kurslara kayıtlı öğrenci sayısını bul. (`course_name`, `student_count` — `course_id`'ye göre sıralı)

8. Her kursun adını ve bu kursu veren **öğretmenin adını** getir. (`course_name`, `instructor_name` — `course_id`'ye göre sıralı)

9. Hiçbir kursa **kayıtlı olmayan** öğrencileri listele. (Tüm sütunlar)

10. Kurslara göre **ortalama öğrenci yaşı** nedir? (`course_name`, `avg_age` — `course_name`'e göre alfabetik sıralı)

### Bölüm 3: İleri JOIN ve GROUP BY

11. Öğrenci başına toplam kaç kursa kayıtlı olduklarını listele. (`first_name`, `last_name`, `total_courses` — `student_id`'ye göre sıralı)

12. **Birden fazla** kurs veren öğretmenleri listele. (`instructor_name`, `total_courses`)

13. Kurslara göre kaç **farklı** öğrenci kayıtlı? (`course_name`, `unique_students` — `course_name`'e göre alfabetik sıralı)

14. Hem **'SQL Temelleri'** hem de **'İleri SQL'** kursuna kayıtlı öğrencileri bul. (`first_name`, `last_name`)

15. Kurs, öğretmen ve öğrenciyi birleştirerek kayıt tarihlerini listele. (`first_name`, `last_name`, `course_name`, `instructor_name`, `enrollment_date` — `enrollment_id`'ye göre sıralı)

---

## İpucu: Ayrı Schema Kullanmak

Localinizdeki PostgreSQL'de başka tablolarla karışmasın istiyorsanız, yeni bir schema oluşturabilirsiniz:

```sql
CREATE SCHEMA data2;
```

Ardından `scripts/init_db.py` içindeki tablo isimlerinin başına schema adını ekleyin:

```sql
CREATE TABLE data2.students ( ... );
CREATE TABLE data2.courses ( ... );
```

Foreign key (REFERENCES) tanımlarında da schema adını eklemeyi unutmayın:

```sql
CREATE TABLE data2.enrollments (
    ...
    student_id INT REFERENCES data2.students(student_id),
    ...
);
```

Sorgularınızda da aynı şekilde schema adını kullanmayı unutmayın:

```sql
SELECT * FROM data2.students;
```

> **Önemli:** Bu sadece localinizde çalışırken kolaylık için. Kodunuzu pushlarken schema öneki olmadan bırakın, CI/CD ortamında `public` schema kullanılıyor.
