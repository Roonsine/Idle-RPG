from config import DATA_DIR

from Engine.resource_loader import ResourceLoader


loader = ResourceLoader(DATA_DIR)


game_data = loader.load_all()


print(
    game_data.items.get("oak_log")
)


print(
    game_data.trees.get("oak_tree")
)


print(
    game_data.skills.get("woodcutting")
    
)
print(
    game_data.skills.get("mining")
    
)

print(
    game_data.monsters.get("cow")
)