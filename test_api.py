import requests
import pytest

# الرابط الأساسي للـ API (موقع تجريبي مجاني)
BASE_URL = "https://reqres.in/api"

class TestUserAPI:
    
    # 1. اختبار جلب قائمة المستخدمين
    def test_get_users(self):
        response = requests.get(f"{BASE_URL}/users?page=1")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert len(data["data"]) > 0

    # 2. اختبار إنشاء مستخدم جديد
    def test_create_user(self):
        payload = {
            "name": "Abdelhamed",
            "job": "QA Engineer"
        }
        response = requests.post(f"{BASE_URL}/users", json=payload)
        assert response.status_code == 201 # 201 تعني تم الإنشاء بنجاح
        data = response.json()
        assert data["name"] == "Abdelhamed"
        assert "id" in data # التأكد من أن السيرفر أرجع ID

    # 3. اختبار جلب مستخدم غير موجود (يجب أن يفشل)
    def test_get_unknown_user(self):
        response = requests.get(f"{BASE_URL}/users/23")
        assert response.status_code == 404 # 404 تعني غير موجود