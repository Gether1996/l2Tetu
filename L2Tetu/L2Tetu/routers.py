class CustomRouter:
    def db_for_read(self, model, **hints):
        """
        Return the name of the database to use for read operations on the model.
        """
        if model._meta.app_label == 'accounts':
            return 'login_db'  # Use 'login_db' for this app
        return 'default'  # Use 'default' for all other apps

    def db_for_write(self, model, **hints):
        """
        Return the name of the database to use for write operations on the model.
        """
        if model._meta.app_label == 'accounts':
            return 'login_db'  # Use 'login_db' for this app
        return 'default'  # Use 'default' for all other apps

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow or deny a relation between two objects.
        """
        if obj1._meta.app_label == 'accounts' or obj2._meta.app_label == 'accounts':
            return True  # Allow relations within the same app
        return None  # Default behavior for other relations

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Decide whether to allow a model to be synchronized with a specific database.
        """
        if app_label == 'accounts':
            return db == 'login_db'  # Allow migrations only for 'login_db'
        return None  # Default behavior for other apps and databases