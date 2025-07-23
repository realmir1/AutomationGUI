


# Hastane Yönetim Sistemi




## 🚀 Hakkında

Bu proje, Python'ın Tkinter kütüphanesi kullanılarak geliştirilmiş basit bir **Hastane Yönetim Sistemi** uygulamasıdır. Uygulama, hasta bilgilerini, reçete detaylarını ve ilaç verilerini yönetmek için tasarlanmıştır. Veriler, NoSQL veritabanı olan **MongoDB**'de saklanır.

Bu sistem, hastane personelinin hasta kayıtlarını kolayca oluşturmasına, görüntülemesine, güncellemesine ve silmesine olanak tanır. Kullanıcı dostu arayüzü sayesinde ilaç bilgileri ve hasta detayları hızlıca işlenebilir.

-----

## ✨ Özellikler

  * **Hasta Bilgileri Yönetimi:** Hasta adı, kimlik numarası, doğum tarihi, adres gibi temel hasta bilgilerini kaydedin ve güncelleyin.
  * **Reçete Oluşturma:** Seçilen ilaçlara ve dozajlara göre dinamik reçeteler oluşturun.
  * **İlaç Yönetimi:** Kapsamlı bir ilaç listesinden seçim yapın (ağrı kesiciler, antibiyotikler, kalp ilaçları vb.).
  * **Veri Saklama:** Tüm hasta ve reçete verilerini güvenli bir şekilde MongoDB'de saklayın.
  * **Veri Güncelleme ve Silme:** Mevcut hasta kayıtlarını kolayca düzenleyin veya silin.
  * **Otomatik Referans Numarası:** Yeni kayıtlar için otomatik olarak referans numarası oluşturma.
  * **Kullanıcı Dostu Arayüz:** Tkinter ile oluşturulmuş sezgisel ve basit bir grafiksel kullanıcı arayüzü.

-----

## 🛠️ Kurulum

Bu projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### Önkoşullar

  * **Python 3.x:** Projeyi çalıştırmak için Python'ın kurulu olması gerekmektedir.
  * **MongoDB:** Bir MongoDB sunucusunun çalışır durumda olması ve `mongodb://localhost:xxxxxx/` adresinden erişilebilir olması gerekmektedir. Eğer kurulu değilse, [MongoDB İndirme Merkezi](https://www.mongodb.com/try/download/community) adresinden edinebilirsiniz.

### Adımlar

1.  **Depoyu Klonlayın:**

    ```bash
    git clone https://github.com/KULLANICI_ADINIZ/HastaneYonetimSistemi.git
    cd HastaneYonetimSistemi
    ```

2.  **Gerekli Kütüphaneleri Yükleyin:**

    ```bash
    pip install pymongo tk
    ```

    (Tkinter genellikle Python ile birlikte gelir, ancak `tk` paketi bazı sistemlerde ayrıca gerekebilir.)

3.  **MongoDB Bağlantısını Kontrol Edin:**
    Uygulama `mongodb://localhost:27017/` adresine bağlanmaya çalışacaktır. MongoDB sunucunuzun çalıştığından emin olun.

-----

## 🖥️ Kullanım

Uygulamayı çalıştırmak için ana Python dosyasını yürütün:

```bash
python your_main_file.py # Dosyanızın adını buraya yazın, örneğin: main.py veya hospital_app.py
```

Uygulama açıldıktan sonra:

  * **Hasta Bilgilerini Girin:** Sol taraftaki "Hasta Bilgileri" bölümüne gerekli bilgileri doldurun.
  * **İlaç Seçimi:** "Tablet Adı" açılır menüsünden bir ilaç seçin.
  * **Reçete Oluştur:** "Reçete Oluştur" butonuna tıklayarak girilen bilgilere göre reçeteyi sağ panelde görüntüleyin.
  * **Veri Kaydet:** "Veri Kaydet" butonuna tıklayarak hasta ve reçete bilgilerini MongoDB'ye kaydedin. Kaydedilen veriler alt kısımdaki tabloya otomatik olarak eklenecektir.
  * **Veri Seçimi:** Tablodaki herhangi bir satıra tıklayarak o hastanın bilgilerini form alanlarına otomatik olarak doldurabilirsiniz.
  * **Güncelle:** Tablodan bir kayıt seçtikten sonra, formda yaptığınız değişiklikleri "Güncelle" butonu ile kaydedin.
  * **Sil:** Tablodan bir kayıt seçip "Sil" butonuna tıklayarak o kaydı veritabanından ve tablodan kaldırın.
  * **Temizle:** Tüm giriş alanlarını ve reçete panelini temizlemek için "Temizle" butonunu kullanın.
  * **Çıkış:** Uygulamadan çıkmak için "Çıkış" butonuna tıklayın.

-----

## 💻 Teknolojiler

  * **Python 3.x**
  * **Tkinter:** Grafiksel kullanıcı arayüzü için.
  * **Pymongo:** MongoDB ile etkileşim için Python sürücüsü.
  * **MongoDB:** NoSQL veritabanı.

-----

## 🤝 Katkıda Bulunma

Katkılarınız bu projenin gelişimine büyük değer katacaktır\! Eğer bir hata bulur veya yeni bir özellik önermek isterseniz:

1.  Bu depoyu (repository) forklayın (fork).
2.  Yeni bir dal (branch) oluşturun: `git checkout -b feature/AmazingFeature`
3.  Değişikliklerinizi yapın ve commit edin: `git commit -m 'Add some AmazingFeature'`
4.  Dalı push edin: `git push origin feature/AmazingFeature`
5.  Bir Pull İstemi (Pull Request) açın.

-----

## 📄 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakınız.

-----


-----
