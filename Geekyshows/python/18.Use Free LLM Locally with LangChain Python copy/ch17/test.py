from langchain_community.llms import Ollama


llm = Ollama(model="gemma2:2b")

# response = llm.invoke("Tell me a joke")

# """
# Why don't scientists trust atoms?

# Because they make up everything! 😊
# """
# print(response)

response = llm.stream("Tell a fictional story")

"""
The old lighthouse keeper, Silas, squinted at the storm raging outside. His beard, white as snow, was flecked with salt spray
, and his weathered hands gripped the railing tightly. For sixty years he had watched the waves crash against the rocky shore
 of Islehaven, keeping watch over the sea-worn island like a sentinel in a forgotten kingdom. 

Tonight, however, something felt different. The wind howled a tune Silas hadn't heard before, and the rhythm seemed almost…mechanical, like the beating of a giant's heart. It was then he noticed it - a glint of green light rising from the depths of the storm.  It pulsed and danced against the churning waves, an unearthly beacon in the darkness.

A shiver ran down his spine. The sea wasn’t just restless tonight; it throbbed with an unknown power. Silas's hand instinctively reached for the worn-out book on ancient lore he kept hidden in his chamber. It was said that only those born under the sign of the Green Moon could hear its whispers. 

As night deepened, he deciphered the book's fragmented words - a tale of the Sea Wraith, a vengeful spirit trapped within the
 depths, who wielded the power of the Green Light to wreak havoc upon the land. It spoke of only one way to appease the creature - a tribute in the form of a song, a song that would bridge the gap between worlds and free the Wraith from its prison. 

But Silas was too old for such journeys. His bones creaked with the weight of years and his eyes struggled to hold the fading
 light of hope. Yet, he couldn't ignore the beckoning call of the green light.  He knew the song – a mournful melody sung by the waves themselves, woven from tales of lost love and forgotten dreams.

Against his better judgment, Silas decided to climb the highest tower of the lighthouse, its weathered stone a testament to time. His frail body was met with resistance, every step a struggle against gravity. But the green light beckoned him forward,
 whispering promises of escape. 

As he reached the topmost lantern, the air crackled with raw energy. The Sea Wraith's song echoed through the storm. A sense of overwhelming sadness filled him, a melody laced with pain and loneliness. He began to hum - his voice weak, hesitant, yet carrying the weight of a lifetime.  A wave crashed against the shore, sending spray towards Silas’ face. It felt like a silent scream of grief, echoing the Sea Wraith's own anguish. 

The green light pulsed faster, then subsided. The wind died down. Slowly, the lighthouse stood its ground against the onslaught of waves. As if from a distance, a single tear fell on the worn-out book in Silas’ chamber. It was a tear not for the loss
 but for acceptance – a tear that acknowledged the power of stories and the courage to confront the unknown.

The Sea Wraith's song ceased. The storm finally subsided. The lighthouse stood tall, its light guiding lost souls home. 
Silas knew his journey was done. His final hymn was heard not by mortal ears but by those who danced with the tides. And as he closed his weary eyes, a faint smile graced his lips. He had sung for an age and finally found solace in the melody of his own life.
"""
for res in response:
    print(res, end="")
