# Generated by Django 3.1.7 on 2021-04-21 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_recheio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem_glutem', models.IntegerField(verbose_name='glutem')),
                ('sem_lactose', models.IntegerField(verbose_name='lactose')),
                ('valor_bolo', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='valor_bolo')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False, verbose_name='id_cliente')),
                ('nome_cliente', models.CharField(max_length=50, verbose_name='nome_cliente')),
                ('telefone_cliente', models.CharField(max_length=15, verbose_name='telefone')),
                ('endereco_cliente', models.CharField(max_length=50, verbose_name='endereco')),
                ('cpf_cliente', models.CharField(max_length=15, verbose_name='cpf')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Cobertura',
            fields=[
                ('id_cobertura', models.AutoField(primary_key=True, serialize=False, verbose_name='cobertura_id')),
                ('nome_cobertura', models.CharField(max_length=50, verbose_name='nome_cobertura')),
                ('descricao_cobertura', models.CharField(max_length=250, verbose_name='descricao_cobertura')),
                ('sem_glutem', models.IntegerField(verbose_name='glutem')),
                ('sem_lactose', models.IntegerField(verbose_name='lactose')),
                ('valor_cobertura', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='valor_cobertura')),
            ],
        ),
        migrations.CreateModel(
            name='Tamanho',
            fields=[
                ('id_tamanho', models.AutoField(primary_key=True, serialize=False, verbose_name='Tamanho')),
                ('nome_tamanho', models.CharField(max_length=50, verbose_name='nome_tamanho')),
                ('valor_tamanho', models.FloatField(max_length=20, verbose_name='valor_tamanho')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id_topping', models.AutoField(primary_key=True, serialize=False, verbose_name='íd_topping')),
                ('nome_topping', models.CharField(max_length=50, verbose_name='nome_topping')),
                ('descricao_topping', models.CharField(max_length=250, verbose_name='descricao_topping')),
                ('valor_topping', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='valor_topping')),
            ],
        ),
        migrations.AddField(
            model_name='recheio',
            name='sem_glutem',
            field=models.IntegerField(default='0', verbose_name='glutem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recheio',
            name='sem_lactose',
            field=models.IntegerField(default='0', verbose_name='lactose'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recheio',
            name='valor_recheio',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=6, verbose_name='valor_recheio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='massa',
            name='sem_lactose',
            field=models.IntegerField(verbose_name='lactose'),
        ),
        migrations.AlterField(
            model_name='massa',
            name='valor_massa',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='valor_massa'),
        ),
        migrations.AlterField(
            model_name='recheio',
            name='descricao_recheio',
            field=models.CharField(max_length=250, verbose_name='descricao_recheio'),
        ),
        migrations.AlterField(
            model_name='recheio',
            name='id_recheio',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id_recheio'),
        ),
        migrations.AlterField(
            model_name='recheio',
            name='nome_recheio',
            field=models.CharField(max_length=50, verbose_name='nome_recheio'),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False, verbose_name='id_pedido')),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='desconto')),
                ('data_hora_pedido', models.DateTimeField(verbose_name='data_pedido')),
                ('data_hora_pedido_finalizado', models.DateTimeField(blank=True, null=True, verbose_name='data_finalizado')),
                ('data_hora_pedido_retirado', models.DateTimeField(blank=True, null=True, verbose_name='data_retirado')),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='valor_total')),
                ('bolo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bolo', verbose_name='Bolo')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente', verbose_name='Cliente')),
            ],
        ),
        migrations.AddField(
            model_name='bolo',
            name='bolo_cobertura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cobertura', verbose_name='Bolo_cobertura'),
        ),
        migrations.AddField(
            model_name='bolo',
            name='bolo_massa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.massa', verbose_name='Boloc_Massa'),
        ),
        migrations.AddField(
            model_name='bolo',
            name='bolo_recheio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.recheio', verbose_name='Bolo_Recheio'),
        ),
        migrations.AddField(
            model_name='bolo',
            name='bolo_tamanho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tamanho', verbose_name='Bolo_Tamanho'),
        ),
        migrations.AddField(
            model_name='bolo',
            name='bolo_topping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topping', verbose_name='Bolo_Topping'),
        ),
    ]
