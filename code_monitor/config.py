from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    """Simple immutable configuration container.

    Attributes:
        app_name: Display name for the app.
        debug: Whether to enable verbose logging behaviors.
        max_items: Soft cap used by certain utilities.
    """

    app_name: str = "CodeMonitor"
    debug: bool = False
    max_items: int = 1000


def toggle_debug(config: AppConfig, value: bool) -> AppConfig:
    """Return a new config with `debug` set to the provided value.

    Parameters:
        config: The original configuration instance.
        value: The desired boolean debug state.

    Returns:
        A new `AppConfig` with updated debug setting.
    """
    return AppConfig(app_name=config.app_name, debug=value, max_items=config.max_items)


def clamp_max_items(config: AppConfig, lower: int = 1, upper: int = 10000) -> AppConfig:
    """Clamp `max_items` to the inclusive range [lower, upper].

    Parameters:
        config: The original configuration instance.
        lower: Inclusive minimum allowed value.
        upper: Inclusive maximum allowed value.

    Returns:
        A new `AppConfig` with `max_items` clamped.
    """
    max_items = max(lower, min(upper, config.max_items))
    return AppConfig(app_name=config.app_name, debug=config.debug, max_items=max_items)


<<<<<<< HEAD
=======

def sub_num(a: int, b: int) -> int:
    """
    Subtracts the second integer from the first.

    Parameters:
        a (int): The number from which `b` will be subtracted.
        b (int): The number to subtract from `a`.

    Returns:
        int: The result of subtracting b from a.yes this is true

    Example:
        >>> sub_num(10, 3)
        7
    """
    return a - b


CONFIG = MonitorConfig()
>>>>>>> 1a169db0400747ca60eb75f65f768cc37c0f63f1
