# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0013_mysqlstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='MysqlConnected',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('db_ip', models.CharField(max_length=30)),
                ('db_port', models.CharField(max_length=10)),
                ('connect_server', models.CharField(max_length=100)),
                ('connect_user', models.CharField(max_length=50, null=True, blank=True)),
                ('connect_db', models.CharField(max_length=50, null=True, blank=True)),
                ('connect_count', models.IntegerField()),
                ('create_time', models.DateTimeField(db_index=True)),
            ],
            options={
                'db_table': 'mysql_connected',
            },
        ),
        migrations.CreateModel(
            name='MysqlStatusHis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('db_ip', models.CharField(max_length=30)),
                ('db_port', models.CharField(max_length=10)),
                ('connect', models.SmallIntegerField(default=0)),
                ('role', models.CharField(default=-1, max_length=30)),
                ('uptime', models.IntegerField(default=-1)),
                ('version', models.CharField(max_length=50)),
                ('max_connections', models.SmallIntegerField(default=-1)),
                ('max_connect_errors', models.BigIntegerField(default=-1)),
                ('open_files_limit', models.IntegerField(default=-1)),
                ('open_files', models.SmallIntegerField(default=-1)),
                ('table_open_cache', models.SmallIntegerField(default=-1)),
                ('open_tables', models.SmallIntegerField(default=-1)),
                ('max_tmp_tables', models.SmallIntegerField(default=-1)),
                ('max_heap_table_size', models.IntegerField(default=-1)),
                ('max_allowed_packet', models.IntegerField(default=-1)),
                ('threads_connected', models.IntegerField(default=-1)),
                ('threads_running', models.IntegerField(default=-1)),
                ('threads_waits', models.IntegerField(default=-1, null=True, blank=True)),
                ('threads_created', models.IntegerField(default=-1)),
                ('threads_cached', models.IntegerField(default=-1)),
                ('connections', models.IntegerField(default=-1)),
                ('aborted_clients', models.IntegerField(default=-1)),
                ('aborted_connects', models.IntegerField(default=-1)),
                ('connections_persecond', models.SmallIntegerField(default=-1)),
                ('bytes_received_persecond', models.IntegerField(default=-1)),
                ('bytes_sent_persecond', models.IntegerField(default=-1)),
                ('com_select_persecond', models.SmallIntegerField(default=-1)),
                ('com_insert_persecond', models.SmallIntegerField(default=-1)),
                ('com_update_persecond', models.SmallIntegerField(default=-1)),
                ('com_delete_persecond', models.SmallIntegerField(default=-1)),
                ('com_commit_persecond', models.SmallIntegerField(default=-1)),
                ('com_rollback_persecond', models.SmallIntegerField(default=-1)),
                ('questions_persecond', models.IntegerField(default=-1)),
                ('queries_persecond', models.IntegerField(default=-1)),
                ('transaction_persecond', models.SmallIntegerField(default=-1)),
                ('created_tmp_tables_persecond', models.SmallIntegerField(default=-1)),
                ('created_tmp_disk_tables_persecond', models.SmallIntegerField(default=-1)),
                ('created_tmp_files_persecond', models.SmallIntegerField(default=-1)),
                ('table_locks_immediate_persecond', models.IntegerField(default=-1)),
                ('table_locks_waited_persecond', models.SmallIntegerField(default=-1)),
                ('key_buffer_size', models.BigIntegerField(default=-1)),
                ('sort_buffer_size', models.IntegerField(default=-1)),
                ('join_buffer_size', models.IntegerField(default=-1)),
                ('key_blocks_not_flushed', models.IntegerField(default=-1)),
                ('key_blocks_unused', models.IntegerField(default=-1)),
                ('key_blocks_used', models.IntegerField(default=-1)),
                ('key_read_requests_persecond', models.IntegerField(default=-1)),
                ('key_reads_persecond', models.IntegerField(default=-1)),
                ('key_write_requests_persecond', models.IntegerField(default=-1)),
                ('key_writes_persecond', models.IntegerField(default=-1)),
                ('innodb_version', models.CharField(default=b'-1', max_length=30)),
                ('innodb_buffer_pool_instances', models.SmallIntegerField(default=-1)),
                ('innodb_buffer_pool_size', models.BigIntegerField(default=-1)),
                ('innodb_doublewrite', models.CharField(default=b'-1', max_length=10)),
                ('innodb_file_per_table', models.CharField(default=b'-1', max_length=10)),
                ('innodb_flush_log_at_trx_commit', models.IntegerField(default=-1)),
                ('innodb_flush_method', models.CharField(default=b'-1', max_length=30)),
                ('innodb_force_recovery', models.IntegerField(default=-1)),
                ('innodb_io_capacity', models.IntegerField(default=-1)),
                ('innodb_read_io_threads', models.IntegerField(default=-1)),
                ('innodb_write_io_threads', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_pages_total', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_pages_data', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_pages_dirty', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_pages_flushed', models.BigIntegerField(default=-1)),
                ('innodb_buffer_pool_pages_free', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_pages_misc', models.IntegerField(default=-1)),
                ('innodb_page_size', models.IntegerField(default=-1)),
                ('innodb_pages_created', models.BigIntegerField(default=-1)),
                ('innodb_pages_read', models.BigIntegerField(default=-1)),
                ('innodb_pages_written', models.BigIntegerField(default=-1)),
                ('innodb_row_lock_current_waits', models.CharField(max_length=100)),
                ('innodb_buffer_pool_pages_flushed_persecond', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_read_requests_persecond', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_reads_persecond', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_write_requests_persecond', models.IntegerField(default=-1)),
                ('innodb_rows_read_persecond', models.IntegerField(default=-1)),
                ('innodb_rows_inserted_persecond', models.IntegerField(default=-1)),
                ('innodb_rows_updated_persecond', models.IntegerField(default=-1)),
                ('innodb_rows_deleted_persecond', models.IntegerField(default=-1)),
                ('query_cache_hitrate', models.CharField(default=b'-1', max_length=10)),
                ('thread_cache_hitrate', models.CharField(default=b'-1', max_length=10)),
                ('key_buffer_read_rate', models.CharField(default=b'-1', max_length=10)),
                ('key_buffer_write_rate', models.CharField(default=b'-1', max_length=10)),
                ('key_blocks_used_rate', models.CharField(default=b'-1', max_length=10)),
                ('created_tmp_disk_tables_rate', models.CharField(default=b'-1', max_length=10)),
                ('connections_usage_rate', models.CharField(default=b'-1', max_length=10)),
                ('open_files_usage_rate', models.CharField(default=b'-1', max_length=10)),
                ('open_tables_usage_rate', models.CharField(default=b'-1', max_length=10)),
                ('create_time', models.DateTimeField(db_index=True)),
            ],
            options={
                'db_table': 'mysql_status_his',
            },
        ),
        migrations.AlterField(
            model_name='mysql_replication_his',
            name='create_time',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterUniqueTogether(
            name='mysql_replication',
            unique_together=set([('db_ip', 'db_port')]),
        ),
        migrations.AlterUniqueTogether(
            name='mysqlstatus',
            unique_together=set([('db_ip', 'db_port')]),
        ),
        migrations.AlterIndexTogether(
            name='mysql_replication',
            index_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='mysql_replication_his',
            index_together=set([('db_ip', 'db_port', 'create_time')]),
        ),
        migrations.AlterIndexTogether(
            name='mysqlstatushis',
            index_together=set([('db_ip', 'db_port', 'create_time')]),
        ),
        migrations.AlterIndexTogether(
            name='mysqlconnected',
            index_together=set([('db_ip', 'db_port', 'create_time')]),
        ),
    ]
