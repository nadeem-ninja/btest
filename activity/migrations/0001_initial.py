# Generated by Django 3.1.6 on 2021-02-10 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(max_length=200)),
                ('tz', models.CharField(choices=[('UTC +14', 'Samoa and Christmas Island/Kiribati'), ('UTC +13:45', 'Chatham Islands/New Zealand'), ('UTC +13', 'New Zealand with exceptions and 4 more'), ('UTC +12', 'Fiji, small region of Russia and 7 more'), ('UTC +11', 'much of Australia and 7 more'), ('UTC +10:30', 'small region of Australia'), ('UTC +10', 'Queensland/Australia and 6 more'), ('UTC +9:30', 'Northern Territory/Australia'), ('UTC +9', 'Japan, South Korea and 5 more'), ('UTC +8:45', 'Western Australia/Australia'), ('UTC +8', 'China, Philippines and 10 more'), ('UTC +7', 'much of Indonesia, Thailand and 7 more'), ('UTC +6:30', 'Myanmar and Cocos Islands'), ('UTC +6', 'Bangladesh and 6 more'), ('UTC +5:45', 'Nepal'), ('UTC +5:30', 'India and Sri Lanka'), ('UTC +5', 'Pakistan and 8 more'), ('UTC +4:30', 'Afghanistan'), ('UTC +4', 'Azerbaijan and 8 more'), ('UTC +3:30', 'Iran'), ('UTC +3', 'Moscow/Russia, Turkey and 20 more'), ('UTC +2', 'Greece and 32 more'), ('UTC +1', 'Germany and 45 more'), ('UTC +0', 'United Kingdom and 24 more'), ('UTC -1', 'Cabo Verde and 2 more'), ('UTC -2', 'Pernambuco/Brazil and South Georgia/Sandwich Is.'), ('UTC -3', 'most of Brazil, Argentina and 9 more'), ('UTC -3:30', 'Newfoundland and Labrador/Canada'), ('UTC -4', 'some regions of Canada and 28 more'), ('UTC -5', 'regions of USA and 14 more'), ('UTC -6', 'some regions of USA and 9 more'), ('UTC -7', 'some regions of USA and 2 more'), ('UTC -8', 'regions of USA and 4 more'), ('UTC -9', 'Alaska/USA and regions of French Polynesia'), ('UTC -9:30', 'Marquesas Islands/French Polynesia'), ('UTC -10', 'small region of USA and 2 more'), ('UTC -11', 'American Samoa and 2 more'), ('UTC -12', 'much of US Minor Outlying Islands')], max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.profile')),
            ],
        ),
    ]