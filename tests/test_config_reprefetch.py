import cabina
from cabina._transparent_environment import TransparentEnvironment


def test_env_config_get_reprefetch():
    environ = {"HOST": "127.0.0.1"}
    env = TransparentEnvironment(environ=environ)

    class Config(cabina.Config, cabina.Section):
        API_HOST = env.str("HOST")

    environ.update({"HOST": "192.168.1.1"})
    Config.prefetch()

    assert Config.API_HOST == "192.168.1.1"
