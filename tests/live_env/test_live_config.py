import cabina
from cabina._live_environment import LiveEnvironment


def test_live_env_config_updated_get():
    environ = {"HOST": "127.0.0.1"}

    env = LiveEnvironment(environ=environ)
    class Config(cabina.Config, cabina.Section):
        API_HOST = env.str("HOST")

    environ.update({"HOST": "192.168.1.1"})

    assert Config.API_HOST == "192.168.1.1"


def test_live_env_config_updated_prefetch_doesnt_matter():
    environ = {"HOST": "127.0.0.1"}

    env = LiveEnvironment(environ=environ)
    class Config(cabina.Config, cabina.Section):
        API_HOST = env.str("HOST")
    Config.prefetch()

    environ.update({"HOST": "192.168.1.1"})

    assert Config.API_HOST == "192.168.1.1"
