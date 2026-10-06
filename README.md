Kullanıcı Kayıt Programı (Basitleştirilmiş Yapı)

Bu proje, temel kullanıcı kayıt mantığını ve birim testlerini (unit tests) içeren basit bir Python uygulamasıdır. Klasör karmaşasını önlemek adına tüm kodlar ana dizinde yer alacak şekilde düzenlenmiştir.

Proje Yapısı

.
├── registration.py       # Ana program ve kullanıcı kayıt fonksiyonları
├── test_registration.py  # Pytest birim testleri
├── pytest.ini            # Test konfigürasyon dosyası
└── README.md             # Proje rehberi


Kurulum ve Hazırlık

Projeyi çalıştırmadan önce Python 3 ve gerekli test kütüphanelerinin yüklü olduğundan emin olun:

pip install pytest pytest-cov pytest-html


Programı Çalıştırma

Kullanıcı kayıt programını doğrudan çalıştırmak için terminalde şu komutu yazın:

python registration.py


Testleri Çalıştırma

Testleri ve kod kapsama (coverage) raporlarını hatasız bir şekilde çalıştırmak için aşağıdaki adımları izleyin:

1. Standart Test Çalıştırma

Tüm birim testleri çalıştırmak için:

python -m pytest


2. HTML Test Raporu Oluşturma

Test sonuçlarını detaylı bir HTML raporu olarak kaydetmek için:

python -m pytest --html=report.html --self-contained-html


3. Kapsama (Coverage) Raporu Oluşturma

Kodun ne kadarının test edildiğini gösteren HTML raporunu üretmek için:

python -m pytest --cov=. --cov-report=html


(Bu komut sonrasında oluşan htmlcov/index.html dosyasını tarayıcınızda açabilirsiniz.)

Yapılandırma (pytest.ini)

Klasörsüz yapıda pytest.ini dosyanızın şu şekilde olması yeterlidir:

[pytest]
testpaths = .
python_files = test_*.py
python_functions = test_*
addopts = -v -rA
