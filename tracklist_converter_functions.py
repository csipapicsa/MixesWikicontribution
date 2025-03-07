# tracklsit converter functions

import re
from datetime import datetime, timedelta

# Format: [MM] - relative. as mix starts at 00:00 the first track stafrts
# 1
tracklist_1 = """[00] DJ Helviofox - Cala A Boca [Kubico]
[03] ?
[...] ...
[09] DJ Danifox - Ai Trabalha Remix
[13] ?
[...] ...
[38] Johnny Bravo - POR FAVOR [House Of Aces]"""

#format: [HH:MM] - absolute time (day) - the mix start at 00:00, so the first track is at 00:00
# 2
tracklist_2 = """[21:05] Jam & Spoon - Follow Me [Jam! - 6598552]
[21:17] Fatboy Slim - Star 69 [Skint - 500575 2]
[21:20] Sander Kleinenberg - Sound Family [Combined Forces - 023]
[21:24] Waah - Pob [Platipus - 78]
[21:29] Bleachin' - Peakin' (Kee Mo Remix) [BMG]
[21:33] Sven Palzer - Stretchin' [Superfly - 10027]
[21:38] Fatboy Slim - Sunset (Bird Of Prey) [Skint - 500575 2]
[21:41] Steve Lawler - Rise 'In (Nalin & Kane Vocal Remix) [Superfly - 20025-2]
[21:47] Rene Et Emanuel - Invader [Superfly - 20029]
[21:50] Sven VÃ¤th - L'esperanza (M. Mayer Remix) [Club Culture - 8573 84842-0]
[21:55] Taiko - Silence [Slot Machine - 0020-6]
[22:00] Mr. X & Mr. Y - Global Players [Electric Kingdom - 74321 812 491]
[22:04] Natious - Amber (Oliver Lieb Remix) [Amato International - 12019 R]
[22:10] Paul Gaarn - Rise Above Me [Telica - 27]
[22:16] Frost - Acid Phase [Acalwan - 9929-12]
[22:20] Kenji Ogura Feat. Melanie Di Tria - KreissÃ¤ge Typ A [Tracid Traxxx - 2024]
[22:23] Chris Liebing - Call It What You Want (Part 4) EP (B) [CLAU - 04]
[22:27] One Eyed Jack - Lets Rock [Meaty Moosic - 003]
[22:32] Ignore Alien Orders - 3708 Virginia [Generator - 914512]
[22:38] Miller & Floyd - Time (Miller Mix) [Grand Casino - 004-6]
[22:44] Sonic Illusions - Alone In Paris [Heaven Beats - 2083]
[22:47] Magnum Force - Unlucky Punk (Thermobee's .44 Calibre Mix) [S.U.F. - SUFR 20]
[22:54] Paul van Dyk - We Are Alive [Vandit - 007a]
[22:58] Marc O' Tool - Stauffenberg [Underworld - 9621-12]
[23:04] The Horrorist - One Night In NYC (Pascal F.E.O.S Remix) [Superstar]
[23:11] Mauro Picotto - Bug [BXR Germany - 1109-12]
[23:15] Junkie XL - Zerotonine (Junkie XL's Extended Neurotransmitter) [Mamifesto - 562858-1]
[23:21] T.P. Heckmann - Dimensions Disco [Sub-Wave - SW 2002]
[23:27] Francesco Farfa Meets Pleasure Team - The Search [Planetary Conciousness - 2026-6]
[23:32] Ray Clarke - No Return [Hardware Files - 0004-12]
[23:36] Liquid Overdose - Contact [Scanner - NN 2000005]
[23:43] Ian Wilkie - Guten Morgen [Polyester - 01]
[23:48] Bismark - Make A Dream [BXR Germany - 1102-12]
[23:55] Ramirez - La Musika Tremenda [Serious Beats - 541416]"""

# format: [MM:SS] - as mix starts at 00:00 the tracklsit starts
# 3
tracklist_3 = """[00:00] Schiller - Das Glockenspiel (Humate Remix)
[02:14] Slusnik Luna - Sun
[08:05] Melonhaus - Asset Stripper
[14:17] The Dream Traveller - Time (Deepsky Mix)
[19:43] Pink Bomb - Indica (Vocal Mix)
[26:24] Salt Tank - Eugina (TiÃ«sto Remix)
[31:30] Goldenscan - Sunrise (TiÃ«sto Remix)
[39:02] The Thrillseekers - Synaesthesia (Thrillseekers Club Mix)
[45:01] Joshua Ryan - Pistolwhip
[50:22] Subtle By Design - Sirius (DJ TiÃ«sto Remix)"""

# format: [MMM] - as mix starts at 00:00 the tracklsit starts
# 4
tracklist_4 = """[000] ?
[001] ?
[003] Surgeon - (Intro) Version II [Tresor - Tresor 85]
[009] ?
[010] Surgeon - La Real (Part 1) [Counterbalance - CBX 002]
[013] Surgeon - Magneze [Downwards - 12 PLINK 6]
[017] Regis - Execution Ground [Downwards - Lino 021]
[019] Regis - Purification [Downwards - Lino 023]
[022] ?
[031] Surgeon - Sleep (Ultra Violet) [Dynamic Tension - DTR LP1]
[034] Joey Beltram - Life Force [Trax - TX 50132]
[037] ?
[039] ?
[...] ...
[056] Vainqueur - Lyot (Maurizio Mix) [Tresor - 10185D]
[058] ?
[...] ...
[078] Regis - Her Surrender [Downwards - DNRECD 3]
[081] ?
[...] ...
[099] Regis - Guiltless [Downwards - DNRECD 2]
[100] ?
[103] Surgeon - La Real (Part 1) [Counterbalance - CBX 002]
[107] ?
[112] Surgeon - Returning To The Purity Of Current [Tresor - 245DTM]
[116] Surgeon - Waiting For Me (Part 1) [Counterbalance - CBX 003]
[117] ?
[121] DJ Sherwen Feat. Ill Billy - Kracktronik Theme (Paul Damage Remix) [Kracktronik - KRAK 001]
[124] ?
[...] ..."""

# format: MMM:SS - as mix starts at 00:00 the tracklsit starts
# 5
tracklist_5 = """[000:00] Vikter Duplaix - City Spirits (King Britt's Scuba Trip) [Groove Attack 85]
[005:30] Little Louie Vega Feat. Arnold Jarvis - Life Goes On (Dub Goes On Mix) [MAW 52]
[013:02] Max Brennan - Choose To Except [Sublime LP016]
[018:52] Latina CafÃ© - Power To Conquer [Yoruba 25]
[022:17] Plutonia - Forever [Visions Inc. 2]
[023:35] File:2000-09-30 Partyservice Saenger ID023.mp3 ?
[032:18] Macy Gray feat. Mos Def - I've Committed Murder (ID Remix)
[039:44] Royce Da 5'9"" - Boom (Instrumental Version) [Game 2009]
[040:22] El-B - Ghetto Girl [Scorpion 001]
[041:58] Allstars - Hotboy (Dub) [Allstars 6]
[045:48] JMD - Time Machine [Metrix 4]
[050:59] 2 Smart - Groovy Day [Draft 22]
[055:24] U. S. Collective - Midnite Luv [SI Project 15]
[062:44] Attica Blues - What Do You Want (King Britt's Scuba Epic) [Higher Ground]
[068:06] Stephane Attias - Brazilian Fight Song [Laws Of Motion 17]
[075:34] Gamat 3000 - Radio Moon [Moon Harbour 1]
[081:23] Blue Six - Pure [Naked Music 8]
[087:03] Jori Hulkkonen - Back When We Was Attached [F Communications 126]
[094:53] Frankman - Chili Con Carne [FM 6]
[099:35] Tony Watson - Passages [Ibadan 25]
[102:29] Charles Webster - Your Life [Peacefrog 98]
[104:20] Psyan - Tha Norm [Bitasweet 1007]
[109:54] Charlie Watts Jim Keltner Project - Airto (Restless Soul Moonshine Mix) [Cyberoctave]
[116:52] D.S.L. & Nate Juan - Loca Blue [Chillifunk 27]
[123:17] Moodymann - Don't You Want My Love [Peacefrog 95]
[129:38] File:2000-09-30 Partyservice Saenger ID129.mp3 ?
[134:06] Georg Levin - When I'm With You [Recreation 5005]
[139:01] File:2000-09-30 Partyservice Saenger ID139.mp3 ?
[148:23] SR Smoothy - Inside Of You (OGU 2040) [For Life 9525]
[154:04] Shazz Feat. Ken Norris - Innerside (Ron Trent's Version Family Affair Movement Vocal) [Distance 1437]
[159:32] Lemon Jelly - His Majesty King Raam [Impotent Fury 2]"""

# format MM:SS - as mix starts at 00:00 the tracklsit starts, category 
tracklist_3_2 = """[00:00] Beachcoma (Live)
[05:43] If I Survive (Live)
[12:47] Snyper (Live)
[20:55] Kid 2000 (Live)
[30:56] Altitude (Live)
[36:33] Finished Symphony (Live)"""

# format H:MM:SS - as mix starts at 00:00 the tracklsit starts
tracklist_6 = """[0:00:00] Jonny Bee - Andromeda [Soluble]
[0:05:43] Deep Sector - Deep Beliefs [Lovezone]
[0:11:21] Ellroy, Jonas Afonso - Subtle Message (Ellroy Remix) [Apollo]
[0:17:07] Darmony - Warm From The Winter [Undertechnical]
[0:20:47] Deep Active Sound - Another Chords [DeepClass]
[0:24:00] Goran Geto - Kosmofonika (Part II) [System]
[0:28:44] Dub Fragments, Donc - Free (Dub Fragments Remix) [Traxacid]
[0:33:58] Andreas Bergmann - Export [Moral Fiber]
[0:37:56] Normen Hood - No Beat To Hide [Opossum]
[0:44:16] Maximono - Stellar [Yippiee]
[0:52:42] Matt Gill - Zavarou [Groove On]
[0:58:26] Ivan Garci - No Lights [DeepWit]
[1:03:38] Marcelo Nassi - My Place [A Casa]
[1:08:54] Andreas Bergmann - Cornflakes [Klopfgeist]
[1:12:02] Alexandro Tachyani, Yoram - Carbon (Yoram Remix) [Ban-Off]
[1:18:01] James Hunter - Two Tallies & A Goonie [Buxton]"""

tracklist_4 = """[000] DJ Koze - Let's Love [International - IRR 016]
[006] Prommer & Barck - Journey (KiNK Remix) [Derwin - 0033]
[012] Sei A - You Can Bring (Axel Boman Remix) [Aus - SIMPLE 1253]
[016] ?
[018] Christopher Rau - How Are You Today [Pampa - 007]
[021] Huxley - Atonement [20:20 Vision - VIS 219D]
[026] Django Django - Hail Bop (Daniel Avery Remix) [Because]
[031] Dave Harman - In The Warm [People That Make The - PTMTM 14]
[036] ?
[041] Christopher Rau - Like Yesterday [Smallville - 24]
[045] Homework - Whipped Cream [Exploited - GH-20]
[052] ?
[...] ...
[059] Guillaume & The Coutu Dumonts - Mederico [Oslo - 003]
[063] Herbert - It's Only (DJ Koze Remix) [Pampa - 012]
[068] ?
[...] ...
[075] Roy Ayers - Tarzan (Ã‚me Remix) [Azuli Back Catalog - AZCD 45UM]
[081] Sebo K - Mr. Duke [Cr2 - ITC2LD 034]
[085] KiNK & Neville Watson - Blueprint [Rush Hour - RH 2009]
[090] Virgo Four - It's A Crime (Caribou Remix) [Balance - BAL 004 CD]
[098] Tuff City Kids - Begger [Unterton - 02]
[101] Freak Seven Feat. Aniff - Nano Kids (Vocal Mix) [Rush Hour - RH 032]
[108] Kulsch - Loreley (Unmixed) [!K7 - K7298 DTM]
[114] ?
[...] ...
[120] Groove Armada - The Pleasure Victim [Moda Black - MB 042IT]
[123] John Tejada - Torque [Palette - PAL-050]
[129] Onsunlade - Envision (Ã‚me Remix) [Balance - BAL 004 CD]
[135] Justus KÃ¶hncke - Advance [Kompakt - KOM 141]
[142] Gingy & Bordello - Iron & Water [Turbo - CD 034]
[147] David August - Roco Coco [Diynamic]
[152] Yes Wizard - Elephant & Castle (Duke Dumont Remix) [Tigersushi - TS 045]
[157] Caribou - Niobe [City Slang - SLANG 1047982]"""

tracklist_4_2 = """[000] ?
[...] ...
[018] Brothers With Soul - Music Is So Special (Tactical Aspect VIP)
[...] ...
[038] Andy Skopes - Who Are You [Inperspective]
[044] Theory feat. Chieftain Joseph - Hi Grade [Rupture LDN]
[050] Equinox - Barcelona (Tearout Version)
[055] Double O - Dreamin' (Unreleased Mix)"""

# format: A number, MM:SS - category 7
tracklist_7 = """01. [00:00] Revival - Take Me To The River (Sophie Lloyd Remix) [Revival]
02. [05:59] Mainline - Heat Up The House [Pleased As Punch]
03. [09:36] AnanÃ© - Let Me Be Your Fantasy (Mousse T.'s Fantastic Shizzle Mix) [Nervous Records]
04. [14:27] Bobby & Steve feat. Gwen Yvette & Peppe Citarella - Let's Go All The Way (Moplen Mix) [White Label]
05. [20:30] Never Dull - Beverly Disco [Never Dull]
06. [24:23] Mick Jackson - Weekend (The Reflex Mix) [White Label]
07. [27:56] Joy Anonymous - Follow Me (Joy Anonymous Bootleg) [White Label]
08. [31:59] Mousse T. - All I Want Is The Bass [Peppermint Jam]
09. [36:46] Ciccio Merolla feat. Clementino & Hellen - TereketÃ¨ (Cassara's Remix) [White Label]
10. [41:38] Towa Tei - Luv Connection (Mousse T.'s Club Mix) [Elektra]
11. [45:44] Mellow Man - Ghettoblaster (Original '79 Version) [Peppermint Jam]
12. [48:17] Mousse T. vs Hot â€˜nâ€™ Juicy â€“ Horny (Juiceppe's 'If It's Nice, Play It Twice' Remix) [White Label]
13. [53:31] Marco Faraone & Greeko â€“ Armaghetton (Aeroplane Remix) x Selace â€“ So Hooked On Your Lovinâ€™ (Mousse T.'s Acapella) [White Label]
14. [57:14] Donna Summer - Je T'aime [Casablanca]"""

tracklist_error = """[00] Odd Mob - Give You [Tinted]
[00] ALL U NEED (CID & Shiba San) - Bring It Back [Toolroom Trax]
[04] Riton & Roro & Ian Asher - Shake, Shake [Polydor]
[07] Mau P - BEATS FOR THE UNDERGROUND [Repopulate Mars]
[11] Nocapz. - Slow Giggle [Encasa]
[13] Hardrive - Deep Inside [Strictly Rhythm]
[16] Guy Mac & Sam Lowe - Iowaska [Subjekt]
[19] Sergio Fernandez - Into The Deep [Blackflag]
[21] Zsak - Take It [There Was Jack]
[24] Low Steppa & Jewel Kid - Big Busta [Toolroom]
[26] Josh Samuel - Allez [Trace Amounts]
[27] EquinÃ¸x - Conmigo [Aeterna]
[31] Vintage Culture & NoMBe - Pleasure Chasers (Joris Voorn Remix) [Vintage Culture]
[34] Dubdogz & DLMT - I Love It [Parade]
[37] Jenn Getz & Alfie Feat. DJ Luck & MC Neat - Bad Bassline [Abode]
[38] Genix & Sandy Chambers - Baby Baby [Anjunabeats]
[40] Armin van Buuren & Camisra - Let Me Show You [Armadaduty Free]
[4?] + BrEaCh - Jack (Acapella) [Dirtybird]
[42] CASSIMM - Feel So Good [There Was Jack]
[44] Cajmere Feat. Dajae - Brighter Days (Marco Lys Remix) [Cajual]
[46] AHADADREAM & Priya Ragu & Skrillex Feat. Contra - TAKA [Major Recordingsffrr]
[47] Antho Decks & Danny Rhys - Yellow Wave [Toolroom]
[50] Jude & Frank & Andruss Feat. TotÃ³ La Momposina - La Luna [Subjekt]
[53] Odd Mob - XTC [Tinted]
[54] CASSIMM & Mahalia Fontaine - Say Yeah [Toolroom]
[57] James Poole - The Surrender [Abode]"""

def calculate_edge_ratio(row):
    # print(row['mix_tracks'])
    # print(f"Cuts: {cuts}")
    try:
        cuts, _, _ = collect_timestamps(row['mix_tracks'])
        # print(f"Cuts: {cuts}")
        max_connections = len(cuts) - 1 if len(cuts) > 1 else 1  # Avoid division by zero
        valid_connections = count_valid_connections(cuts)
        r = int(valid_connections / max_connections)
        if r == 0:
            r = -2
        return r
    except Exception as e:
        print(f"Error processing row: {row}")
        return -1 
    
def count_valid_connections(cuts):
    # Initialize count of valid connections
    valid_connections = 0
    
    # Loop through the list of cuts, stopping before the last item to avoid index error
    for i in range(len(cuts) - 1):
        # Check if current and next node are not None and connect directly
        if cuts[i][1] is not None and cuts[i+1][0] is not None and cuts[i][1] == cuts[i+1][0]:
            valid_connections += 1
    valid_connections = valid_connections * 100
    return valid_connections

def get_timestamp_category(timestamp):
    if re.match(r'^\[\d{2}\]$', timestamp):
        # print(f"Timestamp: {timestamp} - Category: [MM] - 1")
        return 1  # Category: [MM] - Relative time in minutes
    elif re.match(r'^\[\d{2}:\d{2}\]$', timestamp):
        hours = int(timestamp[1:3])
        if hours >= 0 and hours <= 23:
            return 2  # Category: [HH:MM] - Absolute time in hours and minutes
        else:
            return 3  # Category: [MM:SS] - Relative time in minutes and seconds
    elif re.match(r'^\[\d{3}\]$', timestamp):
        return 4  # Category: [MMM] - Relative time in minutes (with leading zeros)
    elif re.match(r'^\[\d{3}:\d{2}\]$', timestamp):
        return 5  # Category: [MMM:SS] - Relative time in minutes and seconds (with leading zeros)
    elif re.match(r'^\[\d{1}:\d{2}:\d{2}\]$', timestamp):
        return 6  # Category: [H:MM:SS] - Relative time in hours, minutes, and seconds
    else:
        return 0  # Unknown category

def cat_2_or_3(tracklist):
    timestamps = re.findall(r'\[(\d{1,3}:\d{2})\]', tracklist)
    if not timestamps:
        return 0  # Unknown category

    min_h_value_cat2 = float('inf')
    max_h_value_cat2 = float('-inf')
    min_h_value_cat3 = float('inf')
    max_h_value_cat3 = float('-inf')

    for timestamp in timestamps:
        parts = timestamp.split(':')
        temp_cat2_h = int(parts[0])
        min_h_value_cat2 = min(temp_cat2_h, min_h_value_cat2)
        max_h_value_cat2 = max(temp_cat2_h, max_h_value_cat2)

        temp_cat3_h = int(parts[0])
        min_h_value_cat3 = min(temp_cat3_h, min_h_value_cat3)
        max_h_value_cat3 = max(temp_cat3_h, max_h_value_cat3)
    
    if max_h_value_cat3 > 23:
        return 3
    elif max_h_value_cat3 - min_h_value_cat3 > 24:
        return 3
    else:
        return 2
    # Category 2 : [HH:MM] - Absolute time in hours and minutes
    # Category 3 : [MM:SS] - Relative time in minutes and seconds

def preprocess_tracklist(tracklist):
    # category 7
    # Regular expression to find and remove leading numbering like "01. "
    preprocessed_tracklist = re.sub(r'^\d{1,2}\.\s+', '', tracklist, flags=re.MULTILINE)
    return preprocessed_tracklist

def get_tracklist_category(tracklist):
    category_counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, "UNK": 0}
    # category 7
    # tracklist = preprocess_tracklist(tracklist)
    lines = tracklist.split('\n')
    
    for line in lines:
        # print(line)
        match = re.match(r'\[([^\]]+)\]', line)
        if match:
            timestamp = match.group(1)
            category = get_timestamp_category(f'[{timestamp}]')
            # print(timestamp, category)
            category_counts[category] += 1
        else:
            category = "UNK"
            category_counts[category] += 1
    
    most_common_category = max(category_counts, key=category_counts.get)
    if most_common_category == 2 or most_common_category == 3:
        most_common_category = cat_2_or_3(tracklist)
     
    return most_common_category


from copy import deepcopy

def node_validity_checker(timestamp_start, next_timestamp, node_validity):
    if next_timestamp != "..." and timestamp_start != "..." and "?" not in next_timestamp and "?" not in timestamp_start:
        node_validity.append(True)
    else:
        node_validity.append(False)
    return node_validity

def category_2_adjuster(timestamp, start):
    if timestamp == "...":
        return "..."
    else:
        timestamp_dt = datetime.strptime(timestamp, "%H:%M")
        start_dt = datetime.strptime(start, "%H:%M")
        
        if timestamp_dt < start_dt:
            # Assuming the list doesn't span more than 24 hours; adjust by adding 24 hours to the timestamp
            timestamp_dt += timedelta(hours=24)
        
        adjusted_dt = timestamp_dt - start_dt
        # Format adjusted datetime to ensure no negative timedelta is produced
        return f"{adjusted_dt.days * 24 + adjusted_dt.seconds // 3600}:{(adjusted_dt.seconds % 3600) // 60}"


# decrapted due to the -1 day stuff
def _category_2_adjuster(timestamp, start):
    if timestamp == "...":
        return "..."
    else:
        timestamp_dt = datetime.strptime(timestamp, "%H:%M")
        start_dt = datetime.strptime(start, "%H:%M")
        adjusted_dt = timestamp_dt - start_dt
        return str(adjusted_dt)

def fill_gaps(time_ranges):
    """
    Fills gaps in a list of time ranges.
    Args:
        time_ranges (list): List of tuples representing
            time ranges. Each tuple should have two elements,
            representing the start and end times.
    Returns:
        list: List of tuples representing the filled time ranges.

    Example:
        [(0, 180), (None, None), (None, None), (540, 780), (None, None), (None, None), (2280, 'end')]
        =>
        [(0, 180), (180, None), (None, 540), (540, 780), (780, None), (None, 2280), (2280, 'end')]

    """
    # Sort the time ranges by their start times


    # Result list initialized with the first tuple from the input
    result = [time_ranges[0]]
    
    # Iterate through the list of tuples starting from the second element
    for i in range(1, len(time_ranges)):
        # Get current tuple
        current_start, current_end = time_ranges[i]
        # Get the last element of the last tuple in result
        last_end = result[-1][1]
        
        # Check if the start of the current tuple is None and the end of the last tuple is an integer
        if current_start is None and isinstance(last_end, int):
            current_start = last_end
        
        # Prepare to update the end of the current tuple in a similar fashion if needed,
        # but this has to look ahead so it is done in the next iteration
        
        # Update the current tuple in the result
        result.append((current_start, current_end))
    
    # Additional loop to fix ends based on the next start, except for the last element
    for i in range(len(result) - 1):
        current_start, current_end = result[i]
        next_start, _ = result[i + 1]
        
        # If current end is None and next start is an integer, update current end
        if current_end is None and isinstance(next_start, int):
            current_end = next_start
        
        # Update the tuple in the result list
        result[i] = (current_start, current_end)
    
    return result

def collect_timestamps(tracklist, debug=False):
    cuts = []
    
    node_validity = []
    tracklist = preprocess_tracklist(tracklist)
    # print(tracklist)

    tracklist_category = get_tracklist_category(tracklist)

    print(f"The tracklist belongs to Category {tracklist_category}")
    category_start = ""
    category_start_init = False

    lines = tracklist.split('\n')
    for i, line in enumerate(lines):
        # print(line)
        if line == "...":
            line = "[...]"
        match = re.match(r'\[([^\]]+)\]', line)
        try:
            timestamp_start = match.group(1)
        except:
            timestamp_start = "..."
        if tracklist_category == 2 and not category_start_init:
            category_start_init = True
            category_start = deepcopy(timestamp_start)
        else:
            None
        try:
            next_timestamp = lines[i+1]
            match = re.match(r'\[([^\]]+)\]', next_timestamp)
            next_timestamp = match.group(1)
            if tracklist_category == 2:
                timestamp_start = category_2_adjuster(timestamp_start, category_start)
                next_timestamp = category_2_adjuster(next_timestamp, category_start)
            cuts.append((timestamp_start, next_timestamp))
            node_validity = node_validity_checker(timestamp_start, next_timestamp, node_validity)
        except:
            # end of loop
            if tracklist_category == 2:
                timestamp_start = category_2_adjuster(timestamp_start, category_start)
                # next_timestamp = category_2_adjuster(next_timestamp, category_start)
            cuts.append((timestamp_start, "LAST"))
            node_validity = node_validity_checker(timestamp_start, next_timestamp, node_validity)
            None
    if debug:
        print(f"Tracklist_Cagegory: {tracklist_category}")
    # print(len(cuts), len(node_validity))
    # print(cuts, node_validity)
    cuts = translate_timestamps_to_seconds(cuts, node_validity, tracklist_category)
    cuts = fill_gaps(cuts)
    return cuts, node_validity, tracklist_category

def convert_time_to_seconds(time_str, last_hour):
    # print(time_str, last_hour)
    # Handle time format and detect day transition
    parts = time_str.split(":")
    hour = int(parts[0])
    minute = int(parts[1])
    seconds = 0 if len(parts) == 2 else int(parts[2])


    # Check for day transition
    if hour < last_hour:
        hour += 24  # Adjust hour for next day
    
    total_seconds = hour * 3600 + minute * 60 + seconds
    return total_seconds

def translate_timestamps_to_seconds(cuts, node_validity, tracklist_category):
    translated_cuts = []
    last_hour = 0  # To keep track of the last parsed hour to detect day change
    for i, (start, end) in enumerate(cuts):
        if node_validity[i]:
            if tracklist_category == 1 or tracklist_category == 4:
                start_seconds = int(start) * 60
                if end == "LAST":
                    end_seconds = "end"
                else:
                    end_seconds = int(end) * 60
            elif tracklist_category == 2 or tracklist_category == 6:
                # fixing problems, typos, etc
                # print(start, end)
                start = start.replace(".", ":")
                end = end.replace(".", ":") if end != "LAST" else end

                # start_parts = start.split(":")
                start_seconds = convert_time_to_seconds(start, last_hour)
                last_hour = int(start.split(":")[0])  # Update last hour after converting start time
                
                # if len(start_parts) == 3:
                #     start_seconds += int(start_parts[2])
                if end == "LAST":
                    end_seconds = "end"
                else:
                    # ok, start to be complicated, but anywas: Replace every "." to ":" in the end part of the end timestamp
                    end_seconds = convert_time_to_seconds(end, last_hour)
                    # if len(end_parts) == 3:
                        # end_seconds += int(end_parts[2])
            elif tracklist_category == 3:
                start_parts = start.split(":")
                start_seconds = int(start_parts[0]) * 60 + int(start_parts[1])
                if end == "LAST":
                    end_seconds = "end"
                else:
                    end_parts = end.split(":")
                    end_seconds = int(end_parts[0]) * 60 + int(end_parts[1])
            elif tracklist_category == 5:
                start_seconds = int(start[:3]) * 60 + int(start[4:])
                if end == "LAST":
                    end_seconds = "end"
                else:
                    end_seconds = int(end[:3]) * 60 + int(end[4:])
            else:
                continue
            
            translated_cuts.append((start_seconds, end_seconds))
        else:
            translated_cuts.append((None, None))
    
    return translated_cuts

# there are some problem with it
def _translate_timestamps_to_seconds(cuts, node_validity, tracklist_category):
    translated_cuts = []
    for i, (start, end) in enumerate(cuts):
        if node_validity[i]:
            if tracklist_category == 1 or tracklist_category == 4:
                start_seconds = int(start) * 60
                if end == "LAST":
                    end_seconds = "end"
                else:
                    end_seconds = int(end) * 60
            elif tracklist_category == 2 or tracklist_category == 6:
                # fixing problems, typos, etc 
                start = start.replace(".", ":")

                start_parts = start.split(":")
                start_seconds = int(start_parts[0]) * 3600 + int(start_parts[1]) * 60
                if len(start_parts) == 3:
                    start_seconds += int(start_parts[2])
                if end == "LAST":
                    end_seconds = "end"
                else:
                    # ok, start to be complicated, but anywas: Replace every "." to ":" in the end part of the end timestamp
                    end = end.replace(".", ":")

                    end_parts = end.split(":")
                    end_seconds = int(end_parts[0]) * 3600 + int(end_parts[1]) * 60
                    if len(end_parts) == 3:
                        end_seconds += int(end_parts[2])
            elif tracklist_category == 3:
                start_parts = start.split(":")
                start_seconds = int(start_parts[0]) * 60 + int(start_parts[1])
                if end == "LAST":
                    end_seconds = "end"
                else:
                    end_parts = end.split(":")
                    end_seconds = int(end_parts[0]) * 60 + int(end_parts[1])
            elif tracklist_category == 5:
                start_seconds = int(start[:3]) * 60 + int(start[4:])
                if end == "LAST":
                    end_seconds = "end"
                else:
                    end_seconds = int(end[:3]) * 60 + int(end[4:])
            else:
                continue
            
            translated_cuts.append((start_seconds, end_seconds))
        else:
            translated_cuts.append((None, None))
    
    return translated_cuts