import psycopg2

## Bu değeri localinde çalışırken kendi passwordün yap. Ama kodu pushlarken 'postgres' olarak bırak.
password = 'postgres'


def connect_db():
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password=password)
    return conn


def question_1_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students WHERE age > 22;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_2_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM courses WHERE category = %s;', ('Veritabanı',))
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_3_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students WHERE first_name LIKE %s;', ('A%',))
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_4_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM courses WHERE course_name LIKE %s;', ('%SQL%',))
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_5_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students WHERE age BETWEEN 22 AND 24;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_6_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT first_name, last_name FROM students s WHERE EXISTS (SELECT 1 FROM enrollments e WHERE e.student_id = s.student_id) ORDER BY student_id;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_7_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, COUNT(e.student_id) AS student_count FROM courses AS c LEFT JOIN enrollments AS e ON c.course_id = e.course_id WHERE c.category = %s GROUP BY c.course_name;', ('Veritabanı',))
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_8_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, i.name FROM courses AS c JOIN course_instructors AS ci ON c.course_id = ci.course_id JOIN instructors AS i ON ci.instructor_id = i.instructor_id;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_9_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT s.student_id, s.first_name, s.last_name, s.email, s.age FROM students AS s LEFT JOIN enrollments AS e ON s.student_id = e.student_id WHERE e.enrollment_id IS NULL;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_10_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, AVG(s.age) AS avg_age FROM courses AS c JOIN enrollments AS e ON c.course_id = e.course_id JOIN students AS s ON e.student_id = s.student_id GROUP BY c.course_name;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_11_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT s.first_name, s.last_name, (SELECT COUNT(*) FROM enrollments AS e WHERE e.student_id = s.student_id) AS course_count FROM students AS s;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_12_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM (SELECT i.name AS instructor_name, (SELECT COUNT(ci.course_id) FROM course_instructors AS ci WHERE ci.instructor_id = i.instructor_id) AS total_courses FROM instructors AS i) AS tablo WHERE total_courses > 1;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_13_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, (SELECT COUNT(*) FROM enrollments AS e WHERE e.course_id = c.course_id) AS student_count FROM courses AS c ORDER BY c.course_name;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_14_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT s.first_name, s.last_name FROM students s JOIN enrollments e ON s.student_id = e.student_id JOIN courses c ON e.course_id = c.course_id WHERE c.course_name = %s INTERSECT SELECT s.first_name, s.last_name FROM students s JOIN enrollments e ON s.student_id = e.student_id JOIN courses c ON e.course_id = c.course_id WHERE c.course_name = %s;', ('SQL Temelleri', 'İleri SQL'))
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_15_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT s.first_name, s.last_name, c.course_name, i.name AS instructor_name, e.enrollment_date FROM students AS s JOIN enrollments AS e ON s.student_id = e.student_id JOIN course_instructors AS ci ON e.course_id = ci.course_id JOIN instructors AS i ON ci.instructor_id = i.instructor_id JOIN courses AS c ON c.course_id = e.course_id  ORDER BY e.enrollment_id;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data