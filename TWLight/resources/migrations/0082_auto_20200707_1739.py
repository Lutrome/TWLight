# Generated by Django 2.0.13 on 2020-07-07 17:39

import TWLight.resources.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("resources", "0081_auto_20200615_2030")]

    operations = [
        migrations.AlterField(
            model_name="accesscode",
            name="partner",
            field=models.ForeignKey(
                limit_choices_to=models.Q(authorization_method=1),
                on_delete=django.db.models.deletion.CASCADE,
                related_name="accesscodes",
                to="resources.Partner",
            ),
        ),
        migrations.AlterField(
            model_name="language",
            name="language",
            field=models.CharField(
                choices=[
                    ("af", "Afrikaans"),
                    ("ar", "العربية"),
                    ("ast", "asturianu"),
                    ("az", "az-latn"),
                    ("be", "беларуская"),
                    ("bg", "български"),
                    ("bn", "বাংলা"),
                    ("br", "brezhoneg"),
                    ("bs", "bosanski"),
                    ("ca", "català"),
                    ("cs", "čeština"),
                    ("cy", "Cymraeg"),
                    ("da", "dansk"),
                    ("de", "Deutsch"),
                    ("dsb", "dolnoserbski"),
                    ("el", "Ελληνικά"),
                    ("en", "English"),
                    ("en-gb", "British English"),
                    ("eo", "Esperanto"),
                    ("es", "español"),
                    ("es-ni", "español nicaragüense"),
                    ("et", "eesti"),
                    ("eu", "euskara"),
                    ("fa", "فارسی"),
                    ("fi", "suomi"),
                    ("fr", "français"),
                    ("fy", "Frysk"),
                    ("ga", "Gaeilge"),
                    ("gd", "Gàidhlig"),
                    ("gl", "galego"),
                    ("he", "עברית"),
                    ("hi", "हिन्दी"),
                    ("hr", "hrvatski"),
                    ("hsb", "hornjoserbsce"),
                    ("hu", "magyar"),
                    ("ia", "interlingua"),
                    ("id", "Bahasa Indonesia"),
                    ("io", "Ido"),
                    ("is", "íslenska"),
                    ("it", "italiano"),
                    ("ja", "日本語"),
                    ("ka", "ქართული"),
                    ("kab", "Taqbaylit"),
                    ("kk", "kk-cyrl"),
                    ("km", "ភាសាខ្មែរ"),
                    ("kn", "ಕನ್ನಡ"),
                    ("ko", "한국어"),
                    ("lb", "Lëtzebuergesch"),
                    ("lt", "lietuvių"),
                    ("lv", "latviešu"),
                    ("mk", "македонски"),
                    ("ml", "മലയാളം"),
                    ("mn", "монгол"),
                    ("mr", "मराठी"),
                    ("my", "မြန်မာဘာသာ"),
                    ("nb", "norsk (bokmål)"),
                    ("ne", "नेपाली"),
                    ("nl", "Nederlands"),
                    ("nn", "norsk (nynorsk)"),
                    ("os", "Ирон"),
                    ("pa", "pa-guru"),
                    ("pl", "polski"),
                    ("pt", "português"),
                    ("pt-br", "português do Brasil"),
                    ("ro", "română"),
                    ("ru", "русский"),
                    ("sk", "slovenčina"),
                    ("sl", "slovenščina"),
                    ("sq", "shqip"),
                    ("sr", "sr-cyrl"),
                    ("sr-latn", "srpski"),
                    ("sv", "svenska"),
                    ("sw", "Kiswahili"),
                    ("ta", "தமிழ்"),
                    ("te", "తెలుగు"),
                    ("th", "ไทย"),
                    ("tr", "Türkçe"),
                    ("tt", "татарча"),
                    ("udm", "удмурт"),
                    ("uk", "українська"),
                    ("ur", "اردو"),
                    ("vi", "Tiếng Việt"),
                    ("zh-hans", "中文（简体）"),
                    ("zh-hant", "中文（繁體）"),
                ],
                max_length=8,
                unique=True,
                validators=[TWLight.resources.models.validate_language_code],
            ),
        ),
    ]