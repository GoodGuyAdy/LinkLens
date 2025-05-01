from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Entity",
            fields=[
                ("entity_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("entity_type", models.CharField(max_length=100)),
                ("entity_name", models.CharField(max_length=500)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("username", models.CharField(max_length=255)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                ("event_id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            ("viewed", "Viewed"),
                            ("liked", "Liked"),
                            ("hated", "Hated"),
                            ("followed", "Followed"),
                            ("blocked", "Blocked"),
                        ],
                        max_length=20,
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "entity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Models.entity"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Models.user"
                    ),
                ),
            ],
        ),
    ]
