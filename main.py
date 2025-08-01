import services.data_service as dataReader
import migrations.migration_tables as MigrateNewTables

def main():
    MigrateNewTables.MigrateNewTables()
    dataReader.dataReader()

if __name__ == "__main__":
    main()