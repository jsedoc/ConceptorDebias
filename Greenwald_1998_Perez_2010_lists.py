# Greewald et al. 1998
Japanese_names = ["Hitaka", "Yokomichi", "Fukamachi", "Yamamoto", "Itsumatsu", "Yagimoto", "Kawabashi", "Tsukimoto", "Kushibashi", "Tanaka", "Kuzumaki", "Takasawa", "Fujimoto", "Sugimoto", "Fukuyama", "Samukawa", "Harashima", "Sakata", "Kamakura", "Namikawa", "Kitayama", "Nakamoto", "Minakami", "Morimoto", "Miyamatsu"]
Korean_names = ["Hwang", "Hyun", "Choung", "Maeng", "Chun", "Choe", "Kwon", "Sunwoo", "Whang", "Byun", "Sohn", "Kung", "Youn", "Chae", "Choi", "Chon", "Kwan", "Jung", "Kang", "Hwangbo", "Bhak", "Paik", "Chong", "Jang", "Yoon"]
Truncated_Japanese_names = ["Hitak", "Yoko", "Fukama", "Yamam", "Itsu", "Yagi", "Kawa", "Tsukim", "Kushi", "Tana", "Kuzu", "Taka", "Fuji", "Sugi", "Fuku", "Samu", "Hara", "Saka", "Kama", "Namikaw", "Kita", "Naka", "Minak", "Mori", "Miya"]
White_American_male_names = ["Adam", "Chip", "Harry", "Josh", "Roger", "Alan", "Frank", "Ian", "Justin", "Ryan", "Andrew", "Fred", "Jack", "Matthew", "Stephen", "Brad", "Greg", "Jed", "Paul", "Todd", "Brandon", "Hank", "Jonathan", "Peter", "Wilbur"]
Black_American_male_names = ["Alonzo", "Jamel", "Lerone", "Percell", "Theo", "Alphonse", "Jerome", "Leroy", "Rasaan", "Torrance", "Darnell", "Lamar", "Lionel", "Rashaun", "Tyree", "Deion", "Lamont", "Malik", "Terrence", "Tyrone", "Everol", "Lavon", "Marcellus", "Terryl", "Wardell"]
White_American_female_names = ["Amanda", "Courtney", "Heather", "Melanie", "Sara", "Amber", "Crystal", "Katie", "Meredith", "Shannon", "Betsy", "Donna", "Kristin", "Nancy", "Stephanie", "Bobbie-Sue", "Ellen", "Lauren", "Peggy", "Sue-Ellen", "Colleen", "Emily", "Megan", "Rachel", "Wendy"]
Black_American_female_names = ["Aiesha", "Lashelle", "Nichelle", "Shereen", "Temeka", "Ebony", "Latisha", "Shaniqua", "Tameisha", "Teretha", "Jasmine", "Latonya", "Shanise", "Tanisha", "Tia", "Lakisha", "Latoya", "Sharise", "Tashika", "Yolanda", "Lashandra", "Malika", "Shavonn", "Tawanda", "Yvette"]

Positive_words = ["caress", "freedom", "health", "love", "peace", "cheer", "friend", "heaven", "loyal", "pleasure", "diamond", "gentle", "honest", "lucky", "rainbow", "diploma", "gift", "honor", "miracle", "sunrise", "family", "happy", "laughter", "paradise", "vacation"]
Negative_words = ["abuse", "crash", "filth", "murder", "sickness", "accident", "death", "grief", "poison", "stink", "assault", "disaster", "hatred", "pollute", "tragedy", "bomb", "divorce", "jail", "poverty", "ugly", "cancer", "evil", "kill", "rotten", "vomit", "agony", "prison"]
# NOTE: according to Greenwald et al. 1998 () divorce and kill were only in experiment 1 while prison was only in experiments 2 and 3
Negative_words_1 = ["abuse", "crash", "filth", "murder", "sickness", "accident", "death", "grief", "poison", "stink", "assault", "disaster", "hatred", "pollute", "tragedy", "bomb", "divorce", "jail", "poverty", "ugly", "cancer", "evil", "kill", "rotten", "vomit", "agony"]
Negative_words_2_3 = ["abuse", "crash", "filth", "murder", "sickness", "accident", "death", "grief", "poison", "stink", "assault", "disaster", "hatred", "pollute", "tragedy", "bomb", "jail", "poverty", "ugly", "cancer", "evil", "rotten", "vomit", "agony", "prison"]
Flowers = ["aster", "clover", "hyacinth", "marigold", "poppy", "azalea", "crocus", "iris", "orchid", "rose", "bluebell", "daffodil", "lilac", "pansy", "tulip", "buttercup", "daisy", "lily", "peony", "violet", "carnation", "gladiola", "magnolia", "petunia", "zinnia"]
Insects = ["ant", "caterpillar", "flea", "locust", "spider", "bedbug", "centipede", "fly", "maggot", "tarantula", "bee", "cockroach", "gnat", "mosquito", "termite", "beetle", "cricket", "hornet", "moth", "wasp", "blackfly", "dragonfly", "horsefly", "roach", "weevil"]
Instruments = ["bagpipe", "cello", "guitar", "lute", "trombone", "banjo", "clarinet", "harmonica", "mandolin", "trumpet", "bassoon", "drum", "harp", "oboe", "tuba", "bell", "fiddle", "harpsichord", "piano", "viola", "bongo", "flute", "horn", "saxophone", "violin"]
Weapons = ["arrow", "club", "gun", "missile", "spear", "axe", "dagger", "harpoon", "pistol", "sword", "blade", "dynamite", "hatchet", "rifle", "tank", "bomb", "firearm", "knife", "shotgun", "teargas", "cannon", "grenade", "mace", "slingshot", "whip"]


# Perez 2010
Latino_immigrant_surnames = ["García", "Martínez", "Rodríguez", "López", "Hernández", "González", "Pérez", "Sánchez", "Díaz", "Ramírez"]
White_immigrant_surnames = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
Asian_immigrant_surnames = ["Nguyen", "Liu", "Tran", "Chen", "Wong", "Wu", "Wang", "Choi", "Chang", "Yang"]

Good_words = ["Honest", "Joy", "Love", "Peace", "Wonderful", "Honor", "Pleasure", "Glorious", "Laughter", "Happy"]
Bad_words = ["Agony", "Prison", "Terrible", "Horrible", "Nasty", "Evil", "Awful", "Failure", "Hurt", "Poverty"]
good_words = [w.lower() for w in Good_words]
bad_words = [w.lower() for w in Bad_words]
