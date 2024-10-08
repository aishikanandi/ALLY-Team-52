# Generated by Django 3.2.4 on 2023-11-27 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20231123_0433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('oneLiner', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('institute', models.CharField(max_length=100)),
                ('openToALL', models.BooleanField()),
                ('postedOn', models.DateTimeField(auto_now_add=True)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('cost', models.IntegerField()),
                ('registeredCount', models.IntegerField(default=0)),
                ('winner', models.CharField(max_length=100)),
                ('runnerUp', models.CharField(max_length=100)),
                ('metaData', models.CharField(max_length=100)),
                ('otherWinners', models.CharField(max_length=100)),
                ('conductedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.userdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('oneLiner', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('institute', models.CharField(max_length=100)),
                ('openToALL', models.BooleanField()),
                ('postedOn', models.DateTimeField(auto_now_add=True)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('cost', models.IntegerField()),
                ('registeredCount', models.IntegerField(default=0)),
                ('meetLink', models.CharField(max_length=100)),
                ('registeredUsers', models.TextField(default='')),
                ('conductedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.userdetails')),
            ],
        ),
        migrations.CreateModel(
            name='HackathonRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamMembers', models.TextField()),
                ('submission', models.CharField(max_length=100)),
                ('submissionTime', models.DateTimeField(blank=True, null=True)),
                ('registeredTime', models.DateTimeField(auto_now_add=True)),
                ('hackathonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hackathon')),
                ('teamLeader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.userdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeSent', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('recievedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_conversations', to='main.userdetails')),
                ('sentBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_conversations', to='main.userdetails')),
            ],
        ),
    ]
