from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from accounts.factories.user import UserFactory
from accounts.models import Wallet
from exchanges.factories.crypto_currency import CryptoCurrencyFactory
from exchanges.models.crypto_currency import CryptoCurrency


class Command(BaseCommand):
    help = 'Seeder is a command to seed the database'

    def add_arguments(self, parser):
        parser.add_argument('-u', '--user', type=int, help='Number of User to create')
        parser.add_argument('-c', '--crypto', type=int, help='Number of Crypto to create')

    def handle(self, *args, **options):
        self.stdout.write('Starting to seed the database...')
        user_count = options['user']
        crypto_count = options['crypto']

        user_instances = []
        user_data_output = []
        crypto_data_output = []

        admin_user = UserFactory()
        admin_user.is_superuser = True
        admin_user.is_staff = True
        admin_user.save()
        user_data_output.append(
            f'\nAdmin User Details:\n'
            f'  Username: {admin_user.username}\n'
            f'  Password: new_password\n'
        )

        admin, _ = get_user_model().objects.get_or_create(username='admin', is_superuser=True, is_staff=True)
        admin.set_password('new_password')
        admin.save()
        user_data_output.append(
            f'\nAdmin User Details:\n'
            f'  Username: {admin.username}\n'
            f'  Password: new_password\n'
        )
        Wallet.objects.get_or_create(user=admin, defaults={'balance': 1000})

        if user_count:
            for i in range(user_count):
                user = UserFactory()
                user_data_output.append(
                    f'\nUser-{user.id} Details:\n'
                    f'  Username: {user.username}\n'
                    f'  Password: new_password\n'
                )
                user_instances.append(user)
                self.print_progress_bar(i + 1, user_count, prefix='User')

        if crypto_count:
            for i in range(crypto_count):
                crypto = CryptoCurrencyFactory()
                crypto_data_output.append(
                    f'\nCrypto-{crypto.id} Details:\t'
                    f'  Name: {crypto.name}\t'
                    f'  Price: {crypto.price}\n'
                )
                self.print_progress_bar(i + 1, crypto_count, prefix='Crypto')

            instance, _ = CryptoCurrency.objects.get_or_create(name='ABAN', price=20)
            crypto_data_output.append(
                f'\nCrypto-{instance.name} Details:\t'
                f'  Name: {instance.name}\t'
                f'  Price: {instance.price}\n'
            )

        for output in user_data_output:
            self.stdout.write(self.style.NOTICE(output))

        for output in crypto_data_output:
            self.stdout.write(self.style.NOTICE(output))

        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))

    def print_progress_bar(self, iteration, total, prefix='applying', suffix='', length=20):
        """
        Call in a loop to create a terminal progress bar.
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            length      - Optional  : character length of bar (Int)
        """
        percent = 100 * (iteration / float(total))
        filled_length = int(length * iteration // total)
        bar = '⣿' * filled_length + ' ' * (length - filled_length)

        if iteration < total:
            color_start = '\033[94m'
        else:
            color_start = '\033[92m'

        color_end = '\033[0m'

        progress = f'{prefix} [{color_start}{bar}{color_end}] {percent:.1f}% {suffix}'
        self.stdout.write(f'\r{progress}', ending='')
        if iteration == total:
            self.stdout.write('\n')
