from setup import db, Event, Proposal, Organizer, Subscription
session = db.session

'''
class Event(db.Model):
	Must >> 
    id
    speakerHome = "<firstname>\n<secondname>"
    speaker 
    speakerTitle = <status, profession etc>
    imageNameHome  
    imageNameDetail 
    location
    description
    category
    decided
    red
    green
    blue
    organizer 

    If decided >> 
    time  = "<hh:mm - hh:mm AM/PM>"
    weekday = <full weekday>
    date = "<Mmm dd>"
    season = "<Fall/Spring>"
    year = "<yyyy>"
    start = "<yyyy/mm/dd hh:mm>"
	end = "<yyyy/mm/dd hh:mm>"

	If undecided >> 
	start = as much info as possible "<yyyy/mm/dd hh:mm>"
	start = as much info as possible "<yyyy/mm/dd hh:mm>"
    
 	Option>>
    bundle = db.Column(db.String(20))
    background = db.Column(db.String(20))
    funding = db.Column(db.Boolean, default=False)
'''
Wood = Event(
	id = "6", 
	speakerHome = "Melanie\nWood",
    speaker= "Melanie Matchett Wood",
    speakerTitle = "Mathematician",
    imageNameHome = "WoodH.png",  
    imageNameDetail = "WoodD.png",
    location = "SCI 101",
    description = "Melanie Wood is a mathematician at University of California, Berkeley who became the first female to make the US International Mathematical Olympiad Team. Wood graduated from Duke University where she won a Gates Cambridge Scholarship, Fulbright fellowship, and a National Science Foundation graduate fellowship, in addition to becoming the first American woman and second woman overall to be named a Putnam Fellow. She also won the Morgan Prize for her work in Belyi-extending maps and P-orderings, making her the first woman to win this award.",
    category = "Mathematics",
    decided = True,
    red = 1,
    green = .8,
    blue = .2,
    organizer = "Mathematics Dept",
    time  = "4:15 – 5:30PM",
    weekday = "Tuesday",
    date = "Mar 17",
    season = "Spring",
    year = "2020",
    start = "2020/03/17 16:15",
	end = "2020/03/17 18:30")
session.add(Wood)
session.commit()

Topaz = Event(
    id = "7", 
    speakerHome = "Chad\nTopaz",
    speaker= "Chad Topaz",
    speakerTitle = "Mathematician",
    imageNameHome = "TopazH.png",  
    imageNameDetail = "TopazD.png",
    location = "SCI 199",
    description = "Chad Topaz is an applied mathematician and data scientist at Williams College. Since 2016, he continuously received supports from National Science Foundation for his research on nonlinear systems. His work examines natural science problems using methods from data science, modeling, analysis, topology, geometric dynamical systems, numerical simulation. Topaz’s other stream of researches apply quantitative tools to expose and remedy social injustice, and is based out of the Institute for the Quantitative Study of Inclusion, Diversity, and Equity (QSIDE), which he founded.",
    category = "Mathematics",
    decided = True,
    red = .6,
    green = .2,
    blue = .2,
    organizer = "Mathematics Dept",
    time  = "4:15 – 5:30PM",
    weekday = "Tuesday",
    date = "Mar 24",
    season = "Spring",
    year = "2020",
    start = "2020/03/24 16:15",
    end = "2020/03/24 18:30")
session.add(Topaz)
session.commit()

Benn = Event(
    id = "8",
    speakerHome = "Emma\nBenn",
    speaker = "Emma Benn", 
    speakerTitle = "Mathematician", 
    imageNameHome = "BennH.png",
    imageNameDetail = "BennD.png",
    location = "SCI 199",
    description = "Emma K. T. Benn is an Associate Professor in the Department of Population Health Science and Policy at the Icahn School of Medicine at Mount Sinai. She graduated from Swarthmore College in 2004. She subsequently founded NIH-funded Biostatistics Enrichment Summer Training (BEST) Diversity Program, for which she currently serves on the External Advisory Board. She has contributed her biostatistical expertise to a variety of research areas including epilepsy, traumatic brain injury, opioid adherence, and skin bleaching in African and Afro-Caribbean populations. More recently, Dr. Benn has been focused on applying statistics to health disparities research.",
    category = "Mathematics",
    decided = True,
    red = 1,
    green = .6,
    blue = .2,
    organizer = "Mathematics Dept",
    time  = "4:15 – 5:30PM",
    weekday = "Tuesday",
    date = "Mar 31",
    season = "Spring",
    year = "2020",
    start = "2020/03/31 16:15",
    end = "2020/03/31 18:30")

Benn = Event(
    id = "8",
    speakerHome = "Emma\nBenn",
    speaker = "Emma Benn", 
    speakerTitle = "Mathematician", 
    imageNameHome = "BennH.png",
    imageNameDetail = "BennD.png",
    location = "SCI 199",
    description = "Emma K. T. Benn is an Associate Professor in the Department of Population Health Science and Policy at the Icahn School of Medicine at Mount Sinai. She graduated from Swarthmore College in 2004. She subsequently founded NIH-funded Biostatistics Enrichment Summer Training (BEST) Diversity Program, for which she currently serves on the External Advisory Board. She has contributed her biostatistical expertise to a variety of research areas including epilepsy, traumatic brain injury, opioid adherence, and skin bleaching in African and Afro-Caribbean populations. More recently, Dr. Benn has been focused on applying statistics to health disparities research.",
    category = "Mathematics",
    decided = True,
    red = 1,
    green = .6,
    blue = .2,
    organizer = "Mathematics Dept",
    time  = "4:15 – 5:30PM",
    weekday = "Tuesday",
    date = "Mar 31",
    season = "Spring",
    year = "2020",
    start = "2020/03/31 16:15",
    end = "2020/03/31 18:30")

Pettit = Event(
    id = "2",
    start = "2020/08",
    end = "2020/08",
    speakerHome = "Philip\nPettit",
    speaker = "Philip Pettit",
    speakerTitle = "Philosophy Professor",
    time = "4:30 - 6 PM",
    season = "Fall",
    year = "20",
    imageNameHome= "PettitH.png",
    imageNameDetail = "PettitD.png",
    category = "Philosophy",
    location = "Mccabe Atrium",
    decided = False,
    red = 0.2,
    green = 0.2,
    blue = 0.4,
    organizer = "PPE Club",
    description = "Philip Pettit is the Laurence S. Rockefeller University Professor of Politics and Human Values at Princeton University, where he has taught political theory and philosophy since 2002. He works in moral and political theory and on background issues in the philosophy of mind and metaphysics.")
session.add(Pettit)
session.commit()

Rumelin = Event(
    id = "3",
    start = "2020/08",
    end = "2020/08",
    speakerHome = "Julian\nNida\nRumelin",
    speaker = "Julian Nida Rumelin",
    speakerTitle = "Philosophy Professor",
    time = "4:30 - 6 PM",
    season = "Fall",
    year = "20",
    imageNameHome = "RumelinH.png",
    imageNameDetail = "RumelinD.png",
    category = "Philosophy",
    location = "Mccabe Atrium",
    decided = False,
    red = 1,
    green = 0.6,
    blue = 0.2,
    organizer = "PPE Club",
    description = "Julian Nida-Rümelin (born November 28, 1954) is a German philosopher and public intellectual. He served as State Minister for Culture of the Federal Republic of Germany under Chancellor Schröder. Nida-Rümelin propounds an approach to practical philosophy based on his theory of “Structural Rationality.” As an alternative to consequentialism, it avoids the dichotomy between moral and extra-moral rationality that is typical in Kantian approaches, and is thus able to integrate a vast complexity of practical reasons that result in coherent practice.")
session.add(Rumelin)
session.commit()

Simon = Event(
    id = "4",
    start = "2020/01",
    end = "2020/01",
    speakerHome = "David\nSimon",
    speaker = "David Simon",
    speakerTitle = "Producer & Journalist",
    time = "4:30 - 6 PM",
    season = "Spring",
    year = "20",
    imageNameHome = "SimonH(2).png",
    imageNameDetail = "SimonD(1).png",
    category = "Arts",
    location = "Mccabe Atrium",
    decided = False,
    red = 0,
    green = 0.2,
    blue = 0.2,
    organizer = "PPE Club",
    description = "David Simon is best known for his work on The Wire, which is a HBO series about the violent drug trade of Baltimore city. Simon notes that '[The Wire] is a deliberate argument that unencumbered capitalism is not a substitute for social policy; that on its own, without a social compact, raw capitalism is destined to serve the few at the expense of the many.' Before becoming a producer, Simon worked for the Baltimore Sun City Desk for twelve years (1982–95), wrote Homicide: A Year on the Killing Streets (1991), and co-wrote The Corner: A Year in the Life of an Inner-City Neighborhood (1997).")
session.add(Simon)
session.commit()

Math = Organizer(
    id= "Mathematics Dept",
    contact = "msdpt@swarthmore.edu",
    overview = "Swarthmore Department of Mathematics and Statistics hosts guest lectures regularly, known as the math/stat colloquium.")
session.add(List)
session.commit()

List = Organizer(
    id= "List Gallery",
    contact = "apackar1@swarthmore.edu",
    overview = "Each year the List Gallery presents four exhibitions featuring works by distinguished artists. Exhibdemonstrate excellence in the visual arts and engage diverse communities in an ongoing dialogue. Artists raise questions about history, society, and identity, offerring opportunities for interdisciplinary study.")
session.add(List)
session.commit()

PPE = Organizer(
    id = "PPE Club",
    contact = "lguo1@swarthmore.edu",
    overview = "PPE Club meets to discuss questions about Philosophy, Politics, and Economics. It tries to understand people by looking at the forces that shape their lives. It dabbles in various subjects, from virtues to duties, incentives to sentiments, culture to institutions, freedom to power.")
session.add(PPE)
session.commit()
