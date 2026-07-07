"""
موقع صيدلية الشعب — تطبيق Flask
د. محمد حسن
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "al-shaab-pharmacy-secret-key-change-me"

# ---------- بيانات الصيدلية (يمكن تعديلها بسهولة) ----------

PHARMACY = {
    "name": "صيدلية الشعب",
    "doctor": "د. محمد حسن",
    "phone": "01000000000",
    "phone_display": "٠١٠٠٠ ٠٠٠ ٠٠٠",
    "whatsapp": "201000000000",
    "address": "شارع كسرى والزقازيق",
    "email": "info@alshaab-pharmacy.com",
    "hours_weekday": "٨:٠٠ صباحًا — ١٢:٠٠ منتصف الليل",
    "hours_friday": "١٠:٠٠ صباحًا — ١٢:٠٠ منتصف الليل",
    "founded": 1970,
}

SERVICES = [
    {
        "icon": "pill",
        "title": "صرف الأدوية والوصفات",
        "desc": "توفير الأدوية الأصلية بأسعار مناسبة، مع مراجعة دقيقة لكل وصفة طبية قبل الصرف.",
    },
    {
        "icon": "chat",
        "title": "استشارة دوائية مجانية",
        "desc": "د. محمد حسن ومعاونوه متاحون للرد على أي استفسار عن الجرعات والتداخلات الدوائية.",
    },
    {
        "icon": "delivery",
        "title": "توصيل للمنزل",
        "desc": "خدمة توصيل سريعة داخل بورسعيد لكبار السن وأصحاب الهمم وحالات الطوارئ.",
    },
    {
        "icon": "pulse",
        "title": "قياس الضغط والسكر",
        "desc": "قياس مجاني للضغط والسكر مع متابعة دورية لحالات السكري والضغط المزمنة.",
    },
    {
        "icon": "search",
        "title": "توفير الأدوية النادرة",
        "desc": "شبكة توريد واسعة تمكّننا من البحث عن الأدوية غير المتوفرة وتدبيرها في أسرع وقت.",
    },
    {
        "icon": "care",
        "title": "العناية والتجميل",
        "desc": "تشكيلة مختارة من منتجات العناية بالبشرة والشعر من ماركات موثوقة.",
    },
]

TESTIMONIALS = [
    {
        "name": "أم أحمد",
        "text": "الدكتور محمد بيسأل عن حالة والدتي كل شهر من غير ما نطلب، معاملة إنسانية قبل ما تكون شغل.",
    },
    {
        "name": "كريم عادل",
        "text": "لقيت عندهم دواء دورت عليه في أكتر من صيدلية ولقيته عندهم في نفس اليوم.",
    },
    {
        "name": "سارة محمود",
        "text": "خدمة التوصيل ساعدتني كتير وقت ما كنت حامل ومش قادرة أتحرك.",
    },
]


@app.context_processor
def inject_globals():
    return {"pharmacy": PHARMACY, "year": datetime.now().year}


@app.route("/")
def home():
    return render_template("index.html", services=SERVICES[:3], testimonials=TESTIMONIALS)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html", services=SERVICES)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not phone or not message:
            flash("من فضلك املأ كل الحقول قبل الإرسال.", "error")
        else:
            # في الإصدار الحقيقي: احفظ الرسالة في قاعدة بيانات أو أرسلها بالإيميل
            print(f"[رسالة جديدة] {name} - {phone}: {message}")
            flash("تم استلام رسالتك بنجاح، هنتواصل معاك في أقرب وقت.", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
