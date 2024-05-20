# Base Django Backend Projesi

Bu projenin yapılmasının sebebi tekrar tekrar temel yapıların kurulması ile zaman kaybetmemektir.<br>
Bu projede aşağıdaki modüller mevcuttur;
- Login sistemi
- Custom Authentication
- Log Mixin
- Custom Renklendirilmiş Console Log Sistemi
- Jwt Şifreleme

## Kurulum 
Kurulum adımları aşağıdaki gibidir.
1. Environment oluşturulmalıdır. Bu işlemin amacı diğer uygulamalar ile versiyon çakışmalarını önlemektir.İşlem için aşağıdaki kodu console ekranında projenin bulunduğu konuma gelerek çalıştırılması gerekmektedir.
    ```bash
    python -m venv venv
    ```
2. Projenin çalışması için gerekliliklerin yüklemesi için öncelikle oluşturduğumuz environmentin aktif edeilmesi gerekmektedir. Aşağıdaki kodu console ekranında çalıştırılmalıdır.
    ```bash
    source venv/bin/activate
    ```
3. Environment aktif edildikten sonra gerekliliklerin yüklenmesi için aşağıdaki komutun console ekranında çalıştırılması gerekmektedir.
    ```bash
    pip install -r requirements.txt
    ```
4. Projenin ayağa kaldırılması için;