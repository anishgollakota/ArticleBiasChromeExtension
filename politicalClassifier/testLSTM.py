import pickle
import keras
from keras_preprocessing import sequence

def get_score(tweet):
    tweet = [tweet]
    reconstructed_model = keras.models.load_model("lstm_model")

    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    sequences_test = tokenizer.texts_to_sequences(tweet)
    sequences_matrix_test = sequence.pad_sequences(sequences_test, maxlen=100)

    prediction = reconstructed_model.predict(sequences_matrix_test)[0][0]
    return prediction

test_dem_tweet = 'On September 9 — just last week — President Trump unveiled his shortlist of candidates to tap for the Supreme Court should a vacancy open up under his presidency. With Ruth Bader Ginsburg’s death Friday night, he now has that opportunity. The next Trump Supreme Court pick may well come from a list of 20 names he revealed last week, plus a longer list he had already released. The Trump White House and his allies in the Senate have spent years preparing for the next Supreme Court vacancy. Indeed, the judicial selection process may be the one professional and highly competent operation in this administration. Trump has filled the bench with fairly young, impressively credentialed ideologues who will reliably cast very conservative votes if appointed to the Supreme Court, and his Supreme Court shortlist reflects that work. Half of the names that Trump just announced are people he previously appointed to a lower court, and several more are individuals he’s appointed to non-judicial roles. And it doesn’t actually matter all that much which specific name Trump chooses from his list — or whether he ultimately decides to go off-list. Though Trump has kept his promise to only name Supreme Court justices from a prereleased list, he frequently adds new names to it. Neither of Trump’s Supreme Court appointees, Neil Gorsuch and Brett Kavanaugh, was on the original list Trump first released in 2016, but were added in subsequent iterations. What all the names on the list have in common — both old and new — is that they were vetted by Trump’s team (and often by the conservative Federalist Society) to ensure that they are reliable conservatives. That said, there is one important divide among the names on Trump’s list. Some, such as former Solicitor General Paul Clement or Fourth Circuit Judge Allison Jones Rushing, are solid conservatives who aren’t known for over-the-top, Trumpy rhetoric. Others, such as Sens. Ted Cruz (R-TX), Josh Hawley (R-MO), and Tom Cotton (R-AR) are politicians who spent their time in Congress flaunting their conservative bona fides and enraging Democrats. Still others, such as Fifth Circuit Judges James Ho and Kyle Duncan, are sitting judges who take the same trolly approach as Cruz, Hawley, and Cotton, but do so from the bench. The biggest mystery, in other words, is not what the next potential Trump nominee to the Supreme Court might believe, it’s whether Trump would pick someone with a professional demeanor — or choose a professional troll. Who is on Trump’s list? The 20-name list Trump released last week augments an existing list of 25 names that he has released gradually. Most of the names on both lists possess many of the elite credentials one would expect to find in a Supreme Court nominee. Close to half of the individuals on the new list clerked on the Supreme Court shortly after graduating from law school. And, though the lists include a few politicians like the three senators mentioned above and Kentucky Attorney General Daniel Cameron, both lists are dominated by sitting judges — including many Trump appointees. Judge Amy Coney Barrett, of the Seventh Circuit, is a prominent Trump appointee on both lists. She was favored by religious conservatives for Trump’s previous Court pick, perceived as potentially more likely to allow restrictions on abortions than Brett Kavanaugh. Because so many Trump appointees make the list, many of these judges have not served long enough to develop substantial records on the bench. But several of the names on Trump’s new list will raise deep concerns among Democrats. Judge James Ho has spent his not even three years on the United States Court of Appeals for the Fifth Circuit writing opinions that read like something published by Breitbart. His very first judicial opinion was a sweeping attack on campaign finance laws — and it included an entirely gratuitous swipe at the Affordable Care Act. Ho argued that “if you don’t like big money in politics, then you should oppose big government in our lives,” and he cited the Supreme Court’s decision largely upholding Obamacare to drive home his point. Ho has also railed against the “ moral tragedy of abortion ” in an opinion where he accused a fellow federal judge of retaliating “against people of faith for not only believing in the sanctity of life—but also for wanting to do something about it.” Ho’s Fifth Circuit colleague Kyle Duncan, meanwhile, spent much of his pre-judicial career litigating against LGBTQ rights and the right to vote. As a judge, he’s best known for an opinion where he spent more than 10 pages explaining why he insists on referring to a transgender woman using masculine pronouns. Ninth Circuit Judge Lawrence VanDyke is a particularly surprising addition to Trump’s list because VanDyke’s nomination to the federal bench was panned by the American Bar Association due to concerns that VanDyke is too lazy to do the job. “Mr. VanDyke’s accomplishments are offset by the assessments of interviewees that Mr. VanDyke is arrogant, lazy, an ideologue, and lacking in knowledge of the day-to-day practice including procedural rules,” the ABA explained in a scathing letter deeming him unqualified for the federal bench. The ABA’s investigation found that VanDyke “lacks humility, has an ‘entitlement’ temperament, does not have an open mind, and does not always have a commitment to being candid and truthful.” It’s unclear why Trump loyalists would want to see someone appointed to the Supreme Court who may lack the temperament and the work ethic to do the job well. That said, VanDyke is an outlier on Trump’s list. For the most part, the nearly four dozen names Trump has suggested as possible Supreme Court nominees are diligent and highly talented lawyers. They just also happen to be lawyers who are eager to move the law sharply to the right. The White House’s judicial selection process is the most professional operation in the Trump administrationn. To his many critics, “Donald Trump” is a name practically synonymous with goonish incompetence. But Trump’s judicial selection operation is nothing like that. It is both efficient and highly effective in identifying reliable conservative ideologues with sterling legal resumes. In less than four years as president, Trump has appointed 201 lawyers to lifetime appointments on the federal bench, including 53 to powerful seats on the United States Courts of Appeal. By contrast, President Obama appointed only 55 appellate judges during his eight years as president. One reason for this disparity is that Senate Republicans, led by McConnell, imposed a near-total blockade on appeals court confirmations during Obama’s final two years in the White House. That meant that Trump has effectively been able to fill all the appeals court vacancies that arose during his presidency, plus nearly all the vacancies that should have been filled in Obama’s last two years in office. Trump’s judges, moreover, are quite young. “The average age of circuit judges appointed by President Trump is less than 50 years old,” the Trump White House bragged in November of 2019, “a full 10 years younger than the average age of President Obama’s circuit nominees.” And a large percentage of them have amassed impressive credentials such as Supreme Court clerkships and other government jobs of great influence. All of this is a reason for liberals to be more afraid of Trump’s judges — and potential justices — than if Trump were picking undistinguished hacks to fill the bench. Judges of great ability are far more likely to find innovative ways to reshape the law than incompetents and mediocrities. Moreover, Trump is filling the bench with some of the Federalist Society’s brightest minds at the very moment when the judiciary is gaining power relative to the other branches. As I wrote several months ago in a piece laying out Trump’s impact on the bench: In an age of legislative dysfunction, whoever controls the courts controls the country. In the past decade or so — or more precisely, since Republicans took over the House in 2011 — Congress has been barely functional. You can count on one hand — and possibly on just a few fingers — the major legislation it has enacted. Judges, by contrast, have become the most consequential policymakers in the nation. They have gutted America’s campaign finance law and dismantled much of the Voting Rights Act. They have allowed states to deny health coverage to millions of Americans. They’ve held that religion can be wielded as a sword to cut away the rights of others. They’ve drastically watered down the federal ban on sexual harassment. And that barely scratches the surface. If Trump gets to replace a liberal justice, this practice of judicial policymaking will only accelerate. Environmental regulations are likely to be dismantled en masse. Voting rights will be hollowed out even more. Obamacare could be struck down. And, perhaps most significantly, purely partisan Republican arguments will gain even more purchase in the Supreme Court. Anyone Trump names to the Supreme Court, if Trump’s allowed to do so, is likely to push the law relentlessly to the right. Help keep Vox free for all Millions turn to Vox each month to understand what’s happening in the news, from the coronavirus crisis to a racial reckoning to what is, quite possibly, the most consequential presidential election of our lifetimes. Our mission has never been more vital than it is in this moment: to empower you through understanding. But our distinctive brand of explanatory journalism takes resources — particularly during a pandemic and an economic downturn. Even when the economy and the news advertising market recovers, your support will be a critical part of sustaining our resource-intensive work, and helping everyone make sense of an increasingly chaotic world. Contribute today from as little as $3.'
test_rep_tweet = 'President Donald Trump stepped up his rhetoric Thursday on cultural issues, aiming to boost enthusiasm among rural Wisconsin voters as he tries to repeat his path to victory four years ago. Making his fifth visit to the pivotal battleground state this year, Trump views success in the state’s less-populated counties as critical to another term. He held a rally Thursday evening in Mosinee, in central Wisconsin, an area of the state that shifted dramatically toward Republicans in 2016, enabling Trump to overcome even greater deficits in urban and suburban parts of the state. Trump has increasingly used his public appearances to elevate cultural issues important to his generally whiter and older base, as he hinges his campaign on turning out his core supporters rather than focusing on winning over a narrow slice of undecided voters. In Mosinee, he called for a statute to ban burning the American flag in protest — a freedom protected by the Supreme Court — and criticized sports players and leagues for allowing demonstrations against racial inequality. “We have enough politics, right," he said, joking that sometimes, “I can’t watch me.” He added of protests in sports, “People don’t want to see it and the ratings are down.”'
test_dem2_tweet = '"When he nominated her in 1993, Bill Clinton called her “the Thurgood Marshall of gender-equality law”, comparing her advocacy and lower-court rulings in pursuit of equal rights for women to the work of the great jurist who advanced the cause of equal rights for Black people. Ginsburg persuaded the supreme court that the 14th amendment’s guarantee of equal protection applied not only to racial discrimination but to sex discrimination as well. For Ginsburg, principle was everything – not only equal rights, but also the integrity of democracy. Always concerned about the consequences of her actions for the system as a whole, she advised young people “to fight for the things you care about but do it in a way that will lead others to join you”."'
test_label = 0

print(get_score(test_dem2_tweet))