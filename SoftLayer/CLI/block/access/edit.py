"""Modifies a password for a volume's access"""
# :license: MIT, see LICENSE for more details.

import click
import SoftLayer
from SoftLayer.CLI import environment


@click.command()
@click.argument('access_id')
@click.option('--password', '-p', multiple=False,
              help='Password you want to set, this command will fail if the password is not strong')
@environment.pass_env
def cli(env, access_id, password):
    """Modifies a password for a volume's access"""
    block_manager = SoftLayer.BlockStorageManager(env.client)

    result = block_manager.set_credential_password(access_id=access_id, password=password)

    if result:
        click.echo('Password updated for %s' % access_id)
    else:
        click.echo('FAILED updating password for %s' % access_id)
