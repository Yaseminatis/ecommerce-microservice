 
### E-Commerce Microservice System with Dispatcher (API Gateway)

**Kocaeli Üniversitesi**  
**Teknoloji Fakültesi – Bilişim Sistemleri Mühendisliği**  
**Yazılım Geliştirme Laboratuvarı II | Proje 1**

---

## Proje Bilgileri

**Proje Adı:**  E-Commerce Microservice System with Dispatcher (API Gateway) 
**Ders:** Yazılım Geliştirme Laboratuvarı II 
**Akademik Yıl:** 2025 – 2026  

## Ekip Üyeleri

| Ad Soyad | Öğrenci No |
|---------|------------|
| Şenay Cengiz | 231307027 |
| Yasemin Atiş | 231307023 | 

## Tarih
- Mart 2026
##  Giriş

Günümüzde modern yazılım sistemleri, ölçeklenebilirlik ve sürdürülebilirlik açısından monolitik yapılardan mikroservis mimarisine doğru evrilmiştir. Bu projede, mikroservis mimarisi kullanılarak bir e-ticaret sistemi geliştirilmiştir.

Projenin temel amacı, farklı işlevleri bağımsız servisler halinde çalıştırarak, tüm istekleri merkezi bir Dispatcher (API Gateway) üzerinden yöneten, güvenli ve ölçeklenebilir bir sistem oluşturmaktır.

Bu kapsamda:
- Dispatcher, sistemin tek giriş noktası olarak görev yapmaktadır.
- Tüm yetkilendirme işlemleri merkezi olarak Dispatcher üzerinden yapılmaktadır.
- Mikroservisler yalnızca iç ağda çalışacak şekilde izole edilmiştir.
Proje, nesne yönelimli programlama, servis orkestrasyonu, ağ yönetimi ve modern test yaklaşımlarını bir araya getirmektedir.
##  Sonuç ve Tartışma

Bu projede mikroservis mimarisi temel alınarak, Dispatcher (API Gateway) merkezli bir e-ticaret sistemi tasarlanmış ve başarıyla gerçekleştirilmiştir. Geliştirilen sistemde, servisler birbirinden bağımsız çalışacak şekilde yapılandırılmış ve tüm istekler merkezi bir Dispatcher üzerinden yönetilmiştir.

Bu yaklaşım sayesinde sistem hem daha modüler hale getirilmiş hem de ölçeklenebilir ve yönetilebilir bir yapı elde edilmiştir.

---

###  Başarılar

- Mikroservis mimarisi başarıyla uygulanmış ve servisler bağımsız şekilde yapılandırılmıştır.
- Dispatcher, sistemin tek giriş noktası olarak tüm istekleri doğru mikroservislere yönlendirmektedir.
- Yetkilendirme mekanizması merkezi olarak Dispatcher üzerinde gerçekleştirilmiştir.
- Mikroservisler dış dünyaya kapatılarak ağ izolasyonu sağlanmıştır (network isolation).
- Her mikroservis için ayrı MongoDB kullanılarak veri izolasyonu gerçekleştirilmiştir.
- RESTful API prensiplerine uygun endpoint tasarımı yapılmıştır (RMM Seviye 2).
- Dispatcher servisi Test Driven Development (TDD) yaklaşımıyla geliştirilmiştir.
- Locust kullanılarak sistem üzerinde yük testi gerçekleştirilmiş ve performans metrikleri elde edilmiştir.
- Sistem, 50, 100, 200 ve 500 eş zamanlı kullanıcı altında test edilmiş ve stabil çalıştığı gözlemlenmiştir.
- Dispatcher içerisinde geliştirilen özel loglama mekanizması sayesinde:
  - Gelen istekler (method, path, status code, timestamp)
  - Sistem davranışları kayıt altına alınmıştır.
- Monitoring için hazır araçlar yerine sistem içerisinde geliştirilen özel bir çözüm kullanılmıştır:
  - Yük testi sonuçları JSON formatında saklanmıştır (`load_test_results.json`)
  - Bu veriler dashboard arayüzü üzerinden görselleştirilmiştir
  - Trafik yoğunluğu, hata oranı ve yanıt süreleri analiz edilmiştir
- Dashboard arayüzü sayesinde:
  - Trafik analizi
  - Status code dağılımı
  - Performans metrikleri
  - Log kayıtları  
  kullanıcı dostu bir şekilde sunulmuştur.

---

### ⚠️ Sınırlılıklar

- Sistem gerçek üretim ortamı yerine lokal ortamda test edilmiştir.
- Kullanılan kimlik doğrulama mekanizması basit token yapısı ile sınırlıdır (JWT gibi gelişmiş çözümler kullanılmamıştır).
- Mikroservisler arası iletişim yalnızca HTTP üzerinden gerçekleştirilmiştir (asenkron iletişim kullanılmamıştır).
- Geliştirilen monitoring sistemi temel seviyede olup, Grafana ve Prometheus gibi endüstriyel araçlar entegre edilmemiştir.
- Sistem küçük ölçekli veri setleri ile test edilmiştir.
- Yük testi senaryoları belirli sınırlar içinde gerçekleştirilmiştir.

---

### 🚀 Olası Geliştirmeler

- Richardson Maturity Model Seviye 3 (HATEOAS) desteği eklenebilir.
- JWT tabanlı daha güvenli kimlik doğrulama sistemi geliştirilebilir.
- Servisler arası iletişim için Kafka veya RabbitMQ gibi mesajlaşma sistemleri entegre edilebilir.
- Kubernetes kullanılarak sistem orkestrasyonu ve otomatik ölçeklenebilirlik sağlanabilir.
- Grafana ve Prometheus gibi araçlar entegre edilerek daha gelişmiş monitoring altyapısı kurulabilir.
- CI/CD pipeline (GitHub Actions vb.) eklenerek otomatik test ve deployment süreçleri oluşturulabilir.
- Daha büyük veri setleri ve gerçekçi senaryolar ile performans testleri genişletilebilir.

---


### Genel Değerlendirme

Geliştirilen sistem, mikroservis mimarisinin temel prensiplerini başarıyla yansıtmaktadır. Dispatcher üzerinden merkezi kontrol sağlanırken, servisler arası bağımsızlık korunmuştur. Bu sayede sistem hem esnek hem de ölçeklenebilir bir yapıya kavuşmuştur.

Proje sürecinde nesne yönelimli programlama, Test Driven Development (TDD), RESTful API tasarımı, Docker ile konteynerleştirme ve yük testi gibi modern yazılım geliştirme yaklaşımları bir arada kullanılmıştır.

Sonuç olarak, geliştirilen sistem akademik gereksinimleri karşılayan, pratikte uygulanabilir ve geliştirilebilir bir mikroservis mimarisi örneği sunmaktadır.
