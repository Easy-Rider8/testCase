import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.secilstore.com/"
VALID_USERNAME = "test@example.com"  # Geçerli kullanıcı adı
VALID_PASSWORD = "Test1234!"  # Geçerli şifre
INVALID_USERNAME = "fakeuser@example.com"
INVALID_PASSWORD = "WrongPass123"

@pytest.fixture
def login_page(page: Page):
    """Login sayfasını açar"""
    page.goto(BASE_URL)
    return page

def test_ui_01_gecerli_kullanici_ile_giris(login_page):
    """Doğru kimlik bilgileriyle giriş yapılabildiğini doğrula"""
    login_page.get_by_role("textbox", name="Email adresiniz").fill(VALID_USERNAME)  # Kullanıcı adı alanına gir
    login_page.get_by_role("textbox", name="Şifreniz").fill(VALID_PASSWORD)  # Şifre alanına gir
    login_page.click("button:has-text('Giriş Yap')")  # Giriş butonuna tıkla

    expect(login_page).to_have_url(BASE_URL + "home")  # Kullanıcının yönlendirilmesini doğrula

def test_ui_02_gecersiz_kullanici_ile_giris(login_page):
    """Yanlış kimlik bilgileriyle giriş yapıldığında hata mesajını doğrula"""
    login_page.get_by_role("textbox", name="Email adresiniz").fill(INVALID_USERNAME)
    login_page.get_by_role("textbox", name="Şifreniz").fill(INVALID_PASSWORD)
    login_page.click("button:has-text('Giriş Yap')")

    error_message = login_page.locator("div.alert.alert-message")
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("E-Posta,Telefon numarası yada Şifre hatalı")

def test_ui_03_zorunlu_alan_kontrolleri(login_page):
    """Kullanıcı adı ve şifre boş bırakıldığında uyarıları doğrula"""
    login_page.click("button:has-text('Giriş Yap')")  # Boşken girişe bas

    username_alert = login_page.locator("#label-text-alt text-error")
    password_alert = login_page.locator("#label-text-alt text-error")

    expect(username_alert).to_be_visible()
    expect(password_alert).to_be_visible()

def test_ui_04_basarili_giris_sonrasi_yonlendirme(login_page):
    """Başarıyla giriş yapan kullanıcının ana sayfaya yönlendirildiğini doğrula"""
    login_page.get_by_role("textbox", name="Email adresiniz").fill(VALID_USERNAME)
    login_page.get_by_role("textbox", name="Şifreniz").fill(VALID_PASSWORD)
    login_page.click("button:has-text('Giriş Yap')")

    login_page.wait_for_url(BASE_URL + "home")  # Yönlendirme tamamlanana kadar bekle
    assert login_page.url == BASE_URL + "home"
