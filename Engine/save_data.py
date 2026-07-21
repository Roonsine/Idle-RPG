from dataclasses import dataclass, field


@dataclass
class SaveData:
    """
    Represents everything that should be written to disk.
    """

    version: int = 1

    player_name: str = ""

    gold: int = 0

    skills: dict = field(default_factory=dict)

    inventory: dict = field(default_factory=dict)

    equipment: dict = field(default_factory=dict)

    current_action: dict | None = None

    last_saved: str = ""
    
    last_loaded: str = ""