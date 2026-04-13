from sqlalchemy import Column, Integer, String, Date, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Veritabanı yapısını tanımlıyoruz
Base = declarative_base()

class Student(Base):
    __tablename__ = 'student_information'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    grade = Column(Integer)

class LessonProgram(Base):
    __tablename__ = 'lesson_programs'
    lesson_id = Column(Integer, primary_key=True)
    date = Column(Date)
    subject = Column(String)
    activity = Column(String)

class ActivityDetail(Base):
    __tablename__ = 'activity_details'
    activity_id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer, ForeignKey('lesson_programs.lesson_id'))
    description = Column(String)
    materials = Column(String)

# Bilgisayarında geçici bir veritabanı dosyası oluşturur
engine = create_engine('sqlite:///okul_veritabani.db')
Base.metadata.create_all(engine)

# Veritabanı bağlantısını kuruyoruz
Session = sessionmaker(bind=engine)
session = Session()

# Örnek bir kayıt ekleyelim (Test için)
try:
    yeni_ogrenci = Student(name='Ali', surname='Yılmaz', grade=3)
    session.add(yeni_ogrenci)
    session.commit()
    print("Veritabanı başarıyla oluşturuldu ve örnek öğrenci eklendi!")
    
    # Kayıtları ekrana basalım
    ogrenciler = session.query(Student).all()
    print(f"Sistemdeki Öğrenciler: {[o.name + ' ' + o.surname for o in ogrenciler]}")
except Exception as e:
    print(f"Bir hata oluştu: {e}")