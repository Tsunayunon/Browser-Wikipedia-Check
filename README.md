
---

# Tarayıcı Wikipedia Kontrolü

## Proje Genel Bakış

"Tarayıcı Wikipedia Kontrolü", Python ve Selenium WebDriver kullanılarak geliştirilmiş bir otomasyon scriptidir. Bu script, kullanıcının belirttiği web sayfasının başlığında "Wikipedia" kelimesinin geçip geçmediğini kontrol eder. Şu anda Chrome ve Edge tarayıcıları için desteklenmektedir.

## Özellikler

- Chrome ve Edge tarayıcılarında otomatik web sayfası açma.
- Wikipedia'nın Python sayfasına erişim.
- Sayfa başlığında "Wikipedia" kelimesinin varlığını kontrol etme.
- Tarayıcıların güvenli bir şekilde kapatılması.

## Gereksinimler

- Python 3.x
- Selenium kütüphanesi
- ChromeDriver (Chrome için)
- EdgeDriver (Edge için)

## Kurulum

Bu projeyi kullanmadan önce, aşağıdaki adımları tamamlamanız gerekmektedir:

1. Python'u [resmi web sitesinden](https://www.python.org/downloads/) indirip kurun.
2. Selenium kütüphanesini kurun:
   ```
   pip install selenium
   ```
3. Tarayıcınıza uygun WebDriver'ı indirin ve PATH içerisine ekleyin:
   - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
   - [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## Kullanım

Script'i çalıştırmak için, bir terminal veya komut istemi açın, scriptin bulunduğu dizine gidin ve şu komutu çalıştırın:

```sh
python tarayici_wikipedia_kontrolu.py
```

## Katkıda Bulunma

"Tarayıcı Wikipedia Kontrolü" projesine katkıda bulunmak isteyenler, lütfen projeyi forklayın, değişikliklerinizi yapın ve bir pull request gönderin.

## Lisans

Bu proje, MIT Lisansı altında açık kaynaklı olarak sunulmuştur. Detaylar için LICENSE dosyasına bakınız.

---
