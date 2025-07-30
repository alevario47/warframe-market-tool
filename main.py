# Mods list sourced from: https://github.com/RafaelAcuna/WarframeMarket_StandingToPlat/tree/v1.0.1
from modules import get_syndicate, choice

def main():
    syndicate = get_syndicate()
    choice(syndicate)


if __name__ == '__main__':
    main()