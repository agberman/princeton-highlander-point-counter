from argparse import ArgumentParser
import re

parser = ArgumentParser()
parser.add_argument("-d", "--decklist", dest="decklist", help="path to decklist file in text format with each card on a newline and *CMDR* after commanders and *CMPN* after companions")
args = parser.parse_args()

with open(args.decklist) as f:
    deck = f.readlines()

pointed_cards = { 'Ancestral Recall': {'deck': 7}, 'Balance': {'deck': 1},
                'Birthing Pod': {'deck': 1}, 'Black Lotus': {'deck': 7},
                'Channel': {'deck': 2}, 'Chrome Mox': {'deck': 1},
                'Crop Rotation': {'deck': 1}, 'Cyclonic Rift': {'deck': 1},
                'Demonic Tutor': {'deck': 4}, 'Dockside Extortionist': {'deck': 1},
                'Dig Through Time': {'deck': 1},
                'Emrakul, The Aeons Torn': {'deck': 2, 'commander': 2},
                'Fastbond': {'deck': 1}, 'Flash': {'deck': 5},
                "Gaea's Cradle": {'deck': 1}, 'Gifts Ungiven': {'deck': 2},
                "Green Sun's zenith": {'deck': 1}, 'Griselbrand': {'deck': 1, 'commander': 1},
                'Hullbreecher': {'deck': 1}, 'Imperial Seal': {'deck': 1},
                'Intuition': {'deck': 1}, 'Jeweled Lotus': {'deck': 3},
                'Karakas': {'deck': 4}, 'Karn, the Great Creator': {'commander': 1},
                'Leovold, Emissary of Trest': {'deck': 1, 'commander': 7},
                'Library of Alexandria': {'deck': 1}, 'Limited Resources': {'deck': 7},
                'Lutri, the Spellchaser': {'companion': 3}, 'Mana Crypt': {'deck': 4},
                'Mana Drain': {'deck': 1}, 'Mana Vault': {'deck': 1},
                'Merchant Scroll': {'deck': 1}, 'Mox Chrome': {'deck': 1},
                'Mox Diamond': {'deck': 1}, 'Mox Emerald': {'deck': 3},
                'Mox Jet': {'deck': 3}, 'Mox Opal': {'deck': 1}, 'Mox Pearl': {'deck': 3},
                'Mox Ruby': {'deck': 3}, 'Mox Sapphire': {'deck': 3},
                'Mystical Tutor': {'deck': 2}, 'Natural Order': {'deck': 2},
                'Necropotence': {'deck': 2}, 'Paradox Engine': {'deck': 2},
                'Primeval Titan': {'deck': 2}, 'Prophet of Kruphix': {'deck': 2},
                'Protean Hulk': {'deck': 2}, 'Reanimate': {'deck': 1},
                'Recurring Nightmare': {'deck': 1}, 'Rhystic Study': {'deck': 1},
                'Rofellos, Llanowar Emissary': {'deck': 1, 'commander': 1},
                'Sol Ring': {'deck': 4}, 'Spellseeker': {'deck': 2},
                'Smothering Tithe': {'deck': 1}, "Summoner's Pact": {'deck': 1},
                'Survival of the Fittest': {'deck': 2}, 'Sylvan Primordial': {'deck': 1},
                'Tainted Pact': {'deck': 1}, 'Thassa’s Oracle': {'deck': 2},
                'Time Vault': {'deck': 7}, 'Time Walk': {'deck': 7}, 'Tinker': {'deck': 3},
                'Tolarian Academy': {'deck': 1}, 'Transmute Artifact': {'deck': 1},
                'Trade Secrets': {'deck': 3}, 'Treasure Cruise': {'deck': 1},
                'Underworld Breach': {'deck': 2}, 'Vampiric Tutor': {'deck': 2},
                'Wishclaw Talisman': {'deck': 1}, "Yawgmoth's Bargain": {'deck': 1},
                "Yawgmoth's Will": {'deck': 2}, 'Yorion, Sky Nomad': {'companion': 1} }

def get_just_card(messy_text):
    clean_text = messy_text
    if messy_text[0].isdigit():
        clean_text = messy_text.split(' ', 1)[-1]
    if '(' in clean_text:
        clean_text = clean_text.split(' (')[0]
    return clean_text

def main():
    print()
    point_total = 0
    for deck_card in deck:
        for pointed_card in pointed_cards:
            if re.sub(r'[\W_]+', '', pointed_card.lower()) in re.sub(r'[\W_]+', '', deck_card.lower()):
                if '*CMDR*' in deck_card:
                    point_val = pointed_cards[pointed_card]['commander']
                    print(get_just_card(deck_card)+' - '+str(point_val)+' pt. (as commander)')
                    point_total += point_val
                elif '*CMPN*' in deck_card:
                    point_val = pointed_cards[pointed_card]['companion']
                    print(get_just_card(deck_card)+' - '+str(point_val)+' pt. (as companion)')
                    point_total += point_val
                else:
                    if 'deck' in pointed_cards[pointed_card]:
                        point_val = pointed_cards[pointed_card]['deck']
                        print(get_just_card(deck_card)+' - '+str(point_val)+' pt.')
                        point_total += point_val
    print('\n'+str(point_total)+' points total\n')

if __name__ == "__main__":
    main()
