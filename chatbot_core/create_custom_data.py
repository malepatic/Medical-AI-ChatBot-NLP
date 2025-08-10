import pandas as pd

def create_common_disease_dataset():
    """
    Creates a custom dataset for common diseases, with specific variations
    for different demographic groups like age and sex.
    """
    print("Creating custom dataset for common diseases with demographic variations...")
    
    common_diseases_data = [
        {
            "name": "Common Cold",
            "variations": [
                {
                    "group": "Adult (Male/Female)",
                    "prompts": [
                        "I have a runny nose, sneezing, and a sore throat. What could it be?",
                        "What are the symptoms of the common cold for an adult?",
                        "How do you treat a common cold?"
                    ],
                    "completion": "For adults, symptoms like a runny nose, sneezing, and a sore throat often indicate a common cold. Management typically involves rest, staying hydrated, and using over-the-counter medications to relieve symptoms. If symptoms don't improve after 10 days or are accompanied by a high fever, it's best to see a doctor."
                },
                {
                    "group": "Infant (0-1 year)",
                    "prompts": [
                        "My 6-month-old baby has a stuffy nose and is sneezing a lot.",
                        "What should I do if my baby has a cold?",
                        "How to treat a 3-month-old's cold?"
                    ],
                    "completion": "For an infant, a stuffy nose and sneezing can be signs of a cold. It is crucial not to give any over-the-counter cold medicine to babies. Instead, use a saline nasal spray and a bulb syringe to clear their nose, and ensure they are getting plenty of fluids (breast milk or formula). Please consult a pediatrician immediately if the baby has a fever, difficulty breathing, or refuses to feed."
                }
            ]
        },
        {
            "name": "Tension Headache",
            "variations": [
                {
                    "group": "Adult (Male/Female)",
                    "prompts": [
                        "I have a dull, aching pain all over my head. It feels like a tight band.",
                        "What is a tension headache and what should I do?",
                        "My head has been hurting for hours, what should I do?"
                    ],
                    "completion": "A dull, aching sensation across the forehead can be a tension headache. For adults, this can often be managed with over-the-counter pain relievers, rest, and stress-reduction techniques. If headaches become chronic or are severe, consulting a primary care physician is recommended."
                }
            ]
        },
        {
        "name": "Common Cold",
        "variations": [
            {
                "group": "Adult (Male/Female)",
                "prompts": [
                    "I have a runny nose, sneezing, and a sore throat. What could it be?",
                    "What are the symptoms of the common cold for an adult?",
                    "How do you treat a common cold?"
                ],
                "completion": "For adults, symptoms like a runny nose, sneezing, and a sore throat often indicate a common cold. Management typically involves rest, staying hydrated, and using over-the-counter medications to relieve symptoms. If symptoms don't improve after 10 days or are accompanied by a high fever, it's best to see a doctor."
            },
            {
                "group": "Infant (0-1 year)",
                "prompts": [
                    "My 6-month-old baby has a stuffy nose and is sneezing a lot.",
                    "What should I do if my baby has a cold?",
                    "How to treat a 3-month-old's cold?"
                ],
                "completion": "For an infant, a stuffy nose and sneezing can be signs of a cold. It is crucial not to give any over-the-counter cold medicine to babies. Instead, use a saline nasal spray and a bulb syringe to clear their nose, and ensure they are getting plenty of fluids (breast milk or formula). Please consult a pediatrician immediately if the baby has a fever, difficulty breathing, or refuses to feed."
            }
        ]
        },
        {
        "name": "Tension Headache",
        "variations": [
            {
                "group": "Adult (Male/Female)",
                "prompts": [
                    "I have a dull, aching pain all over my head. It feels like a tight band.",
                    "What is a tension headache and what should I do?",
                    "My head has been hurting for hours, what should I do?"
                ],
                "completion": "A dull, aching sensation across the forehead can be a tension headache. For adults, this can often be managed with over-the-counter pain relievers, rest, and stress-reduction techniques. If headaches become chronic or are severe, consulting a primary care physician is recommended."
            }
        ]
        },
        {
        "name": "Sinusitis",
        "variations": [
            {
                "group": "Adult (Male/Female)",
                "prompts": [
                    "I have facial pain and thick yellow nasal discharge for over 10 days",
                    "What are the symptoms of bacterial sinusitis?",
                    "How to tell between sinus infection and cold?"
                ],
                "completion": "Facial pain with thick yellow/green nasal discharge lasting >10 days suggests bacterial sinusitis. Treatment may require antibiotics if symptoms persist beyond 10-14 days. Saline nasal irrigation and decongestants can provide symptom relief. See a doctor if you develop high fever, severe headache, or visual changes."
            },
            {
                "group": "Child (2-12 years)",
                "prompts": [
                    "My 5-year-old has been complaining about cheek pain and has colored mucus",
                    "How to treat sinus infection in children?",
                    "Can kids get chronic sinusitis?"
                ],
                "completion": "In children, cheek pain with colored mucus may indicate sinusitis. Use saline sprays and humidifiers. Antibiotics are rarely needed unless symptoms persist beyond 10 days with fever. Avoid antihistamines as they can thicken mucus. Consult a pediatrician if symptoms worsen or persist."
            }
        ]
        },
        {
        "name": "Contact Dermatitis",
        "variations": [
            {
                "group": "General",
                "prompts": [
                    "I developed an itchy red rash after using new laundry detergent",
                    "What causes skin to react to products?",
                    "How to treat allergic skin reactions?"
                ],
                "completion": "An itchy red rash appearing after exposure to new products suggests contact dermatitis. Wash the area with mild soap, apply hydrocortisone cream 1%, and take oral antihistamines for itching. Identify and avoid the triggering substance. See a dermatologist if rash spreads or blisters develop."
            },
            {
                "group": "Occupational",
                "prompts": [
                    "I work with chemicals and developed dry, cracked hands with rash",
                    "What's the best protection for work-related skin irritation?",
                    "How to treat chemical burns on hands?"
                ],
                "completion": "Occupational contact dermatitis requires: 1) Barrier creams before work 2) Proper PPE (nitrile gloves) 3) Mild cleansers 4) Thick emollients after washing. For active rash, use petroleum jelly under cotton gloves overnight. Consult occupational medicine if persistent."
            }
        ]
    },
    {
        "name": "Plantar Fasciitis",
        "variations": [
            {
                "group": "Adult (Male/Female)",
                "prompts": [
                    "I have sharp heel pain with first steps in the morning",
                    "What causes bottom of foot pain?",
                    "Best exercises for heel pain?"
                ],
                "completion": "Sharp heel pain at morning's first steps suggests plantar fasciitis. Treatment includes: 1) Calf stretches 2) Arch-supporting footwear 3) Night splints 4) Ice massage. Avoid walking barefoot. Consider physical therapy if no improvement after 6 weeks of home treatment."
            },
            {
                "group": "Athletes",
                "prompts": [
                    "I'm a runner with persistent heel pain after workouts",
                    "How to modify training with plantar fasciitis?",
                    "Best running shoes for foot pain?"
                ],
                "completion": "For runners with plantar fasciitis: 1) Reduce mileage by 50% 2) Switch to softer surfaces 3) Use motion-control shoes 4) Add arch supports 5) Cross-train with cycling/swimming. Resume running gradually only when pain-free for 2 weeks. Consider gait analysis."
            }
        ]
    },
    {
        "name": "Restless Legs Syndrome",
        "variations": [
            {
                "group": "Adult (Male/Female)",
                "prompts": [
                    "I get uncomfortable leg sensations at night that improve with movement",
                    "Why do my legs feel restless in bed?",
                    "What deficiency causes restless legs?"
                ],
                "completion": "Unpleasant leg sensations relieved by movement may indicate restless legs syndrome (RLS). Check iron/ferritin levels as deficiency is a common cause. Avoid caffeine/alcohol in evening. Try massage, warm baths, and regular sleep schedule. Consult a neurologist if symptoms disrupt sleep regularly."
            },
            {
                "group": "Pregnancy",
                "prompts": [
                    "I'm pregnant and can't sleep because of creepy-crawly leg feelings",
                    "Is restless legs common in pregnancy?",
                    "Safe treatments for RLS during pregnancy?"
                ],
                "completion": "RLS affects up to 30% of pregnant women, especially in 3rd trimester. Check iron levels - ferritin should be >75 μg/L. Safe options include: 1) Leg massage 2) Warm baths 3) Compression stockings 4) Gentle evening walks. Symptoms usually resolve after delivery."
            }
        ]
    },
    {
        "name": "Bursitis",
        "variations": [
            {
                "group": "General",
                "prompts": [
                    "I have sharp pain in my elbow that's swollen and warm",
                    "What causes fluid-filled sac inflammation?",
                    "How long does elbow bursitis last?"
                ],
                "completion": "Painful, swollen elbow may indicate olecranon bursitis. Treatment includes: 1) Rest 2) Ice packs 3) Compression wrap 4) NSAIDs. Avoid leaning on affected elbow. Most cases resolve in 2-8 weeks. Seek care if redness spreads or fever develops (possible infection)."
            },
            {
                "group": "Knee",
                "prompts": [
                    "There's a squishy lump on my knee that hurts when kneeling",
                    "What is housemaid's knee?",
                    "How to treat prepatellar bursitis?"
                ],
                "completion": "A fluid-filled lump over the kneecap suggests prepatellar bursitis ('housemaid's knee'). Avoid kneeling. Use knee pads if kneeling is unavoidable. Most cases resolve with rest and NSAIDs. Persistent bursitis (>6 weeks) may require aspiration. See doctor if area becomes red/warm."
            }
        ]
    },
    {
        "name": "Raynaud's Phenomenon",
        "variations": [
            {
                "group": "Adult (Female)",
                "prompts": [
                    "My fingers turn white then blue when cold or stressed",
                    "Why do my fingers change color in cold weather?",
                    "Is Raynaud's dangerous?"
                ],
                "completion": "Fingers turning white/blue in cold/stress suggests Raynaud's phenomenon. Keep hands warm with gloves/mittens. Avoid sudden temperature changes and vasoconstrictors (caffeine, nicotine). Most cases are mild, but consult a rheumatologist if you develop finger ulcers or systemic symptoms."
            },
            {
                "group": "Secondary",
                "prompts": [
                    "My Raynaud's symptoms started after beginning new medications",
                    "Can blood pressure meds cause Raynaud's?",
                    "How to tell primary vs secondary Raynaud's?"
                ],
                "completion": "New-onset Raynaud's after medication changes may indicate drug-induced vasospasm. Common culprits include beta-blockers, ADHD medications, and migraine drugs. Consult your prescriber about alternatives. Secondary Raynaud's requires evaluation for underlying autoimmune conditions."
            }
        ]
    },
    {
        "name": "Carpal Tunnel Syndrome",
        "variations": [
            {
                "group": "Office Workers",
                "prompts": [
                    "I get tingling in my hands at night and drop things frequently",
                    "Why do my hands feel numb when typing?",
                    "Best ergonomic setup for wrist pain?"
                ],
                "completion": "Nighttime hand tingling and clumsiness suggest carpal tunnel syndrome. For office workers: 1) Use ergonomic keyboard/mouse 2) Keep wrists neutral 3) Take microbreaks every 30 minutes 4) Try night wrist splints. See doctor if symptoms persist >6 weeks for nerve testing."
            },
            {
                "group": "Pregnancy",
                "prompts": [
                    "I'm pregnant and waking up with numb, painful hands",
                    "Is carpal tunnel common in pregnancy?",
                    "Safe treatments for CTS during pregnancy?"
                ],
                "completion": "Pregnancy-induced carpal tunnel affects up to 60% of women, usually in 3rd trimester. Wear wrist splints at night. Elevate hands when swollen. Most cases resolve postpartum. For severe pain, safe options include acupuncture or corticosteroid injections (after 1st trimester)."
            }
        ]
    },
    {
        "name": "Gout",
        "variations": [
            {
                "group": "Adult (Male)",
                "prompts": [
                    "I woke up with sudden, excruciating pain in my big toe joint",
                    "What foods trigger gout attacks?",
                    "How to tell between gout and infection?"
                ],
                "completion": "Sudden severe big toe pain suggests gout. Avoid: alcohol, red meat, shellfish, high-fructose foods. During attacks: 1) Rest joint 2) Ice 3) NSAIDs 4) Elevate. Colchicine may help if taken early. Recurrent attacks require uric acid-lowering therapy. Different from infection by rapid onset and lack of fever."
            },
            {
                "group": "Postmenopausal",
                "prompts": [
                    "My ankle is red, swollen and too painful to walk on - is this gout?",
                    "Can women get gout after menopause?",
                    "Why did I develop gout after age 60?"
                ],
                "completion": "Postmenopausal women can develop gout due to estrogen decline. Ankle involvement is common in late-onset gout. Manage with: 1) Low-purine diet 2) Hydration 3) Limit alcohol 4) Medications if recurrent. Diuretics for hypertension may contribute - discuss alternatives with your doctor."
            }
        ]
    },
    {
        "name": "Common Cold",
        "variations": [
            {
                "group": "Adult (Male/Female)",
                "prompts": [
                    "I have a runny nose, sneezing, and a sore throat. What could it be?",
                    "What are the symptoms of the common cold for an adult?",
                    "How do you treat a common cold?"
                ],
                "completion": "For adults, symptoms like a runny nose, sneezing, and a sore throat often indicate a common cold. Management typically involves rest, staying hydrated, and using over-the-counter medications to relieve symptoms. If symptoms don't improve after 10 days or are accompanied by a high fever, it's best to see a doctor."
            },
            {
                "group": "Infant (0-1 year)",
                "prompts": [
                    "My 6-month-old baby has a stuffy nose and is sneezing a lot.",
                    "What should I do if my baby has a cold?",
                    "How to treat a 3-month-old's cold?"
                ],
                "completion": "For an infant, a stuffy nose and sneezing can be signs of a cold. It is crucial not to give any over-the-counter cold medicine to babies. Instead, use a saline nasal spray and a bulb syringe to clear their nose, and ensure they are getting plenty of fluids (breast milk or formula). Please consult a pediatrician immediately if the baby has a fever, difficulty breathing, or refuses to feed."
            }
        ]
    },
    {
        "name": "Influenza (Flu)",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have a fever, chills, and muscle aches. Could this be the flu?",
                    "What are the symptoms of influenza in adults?",
                    "How do you treat the flu?"
                ],
                "completion": "For adults, influenza symptoms include fever, chills, cough, sore throat, and body aches. Rest, hydration, and over-the-counter fever reducers can help. Seek medical attention if symptoms are severe, if you have trouble breathing, or if you are in a high-risk group."
            },
            {
                "group": "Elderly",
                "prompts": [
                    "My grandfather has a fever and cough. Should I be concerned about the flu?",
                    "How dangerous is the flu for older adults?",
                    "What should seniors do if they have flu symptoms?"
                ],
                "completion": "Flu can be more dangerous in older adults. Rest, fluids, and close monitoring are important. Seek urgent medical care if there is difficulty breathing, chest pain, confusion, or high fever."
            }
        ]
    },
    {
        "name": "Asthma",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have wheezing and shortness of breath. Could it be asthma?",
                    "What are asthma symptoms in adults?",
                    "How can I manage asthma at home?"
                ],
                "completion": "Asthma symptoms include wheezing, coughing, chest tightness, and shortness of breath. Avoid triggers, use prescribed inhalers, and seek medical help if symptoms worsen or breathing becomes difficult."
            },
            {
                "group": "Child",
                "prompts": [
                    "My child wheezes after running. Could it be asthma?",
                    "How to know if my kid has asthma?",
                    "What should I do if my child has an asthma attack?"
                ],
                "completion": "Children with asthma may wheeze, cough, or get short of breath after activity. Consult a pediatrician for diagnosis and management. If breathing is severely impaired, seek emergency care immediately."
            }
        ]
    },
    {
        "name": "Bronchitis",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have a cough producing mucus and chest discomfort. Could this be bronchitis?",
                    "What are bronchitis symptoms?",
                    "How to recover from bronchitis?"
                ],
                "completion": "Bronchitis symptoms include a persistent cough with mucus, fatigue, and mild fever. Rest, fluids, and avoiding irritants help recovery. If symptoms last more than three weeks or worsen, seek medical advice."
            }
        ]
    },
    {
        "name": "Pneumonia",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have a cough with green mucus and high fever. Could it be pneumonia?",
                    "What are pneumonia symptoms?",
                    "How serious is pneumonia?"
                ],
                "completion": "Pneumonia causes cough, fever, chills, and difficulty breathing. It can be serious and requires prompt medical evaluation, especially in older adults or those with other health conditions."
            },
            {
                "group": "Elderly",
                "prompts": [
                    "My grandmother is weak, confused, and coughing. Could it be pneumonia?",
                    "Is pneumonia dangerous for seniors?",
                    "What should I do if my elderly relative has pneumonia symptoms?"
                ],
                "completion": "In elderly people, pneumonia can cause confusion, weakness, and breathing difficulties. It is a medical emergency — seek immediate professional care."
            }
        ]
    },
    {
        "name": "Hypertension (High Blood Pressure)",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I was told my blood pressure is high. What does this mean?",
                    "What symptoms should I watch for with high blood pressure?",
                    "How can I manage hypertension?"
                ],
                "completion": "High blood pressure often has no symptoms but can lead to heart disease or stroke. Management includes reducing salt intake, regular exercise, stress control, and medical monitoring."
            }
        ]
    },
    {
        "name": "Heart Attack (Myocardial Infarction)",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have chest pain radiating to my left arm. Should I be worried?",
                    "What are the warning signs of a heart attack?",
                    "What should I do if I think I’m having a heart attack?"
                ],
                "completion": "Chest pain with radiation to the arm, jaw, or back, along with sweating, shortness of breath, or nausea, may indicate a heart attack. Call emergency services immediately."
            }
        ]
    },
    {
        "name": "Stroke",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "My face is drooping on one side and I can't move my arm. Could this be a stroke?",
                    "What are stroke symptoms?",
                    "What should I do if I suspect a stroke?"
                ],
                "completion": "Symptoms such as facial droop, weakness on one side, and difficulty speaking are stroke warning signs. Call emergency services immediately — early treatment saves lives."
            }
        ]
    },
        {
        "name": "Gastroenteritis (Stomach Flu)",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have diarrhea, vomiting, and stomach cramps. Could this be the stomach flu?",
                    "What are the symptoms of gastroenteritis?",
                    "How to recover from a stomach bug?"
                ],
                "completion": "Gastroenteritis causes diarrhea, vomiting, and stomach pain, often due to viruses or contaminated food. Rest, stay hydrated, and eat bland foods. Seek care if symptoms persist or signs of dehydration occur."
            },
            {
                "group": "Child",
                "prompts": [
                    "My child has diarrhea and vomiting. What should I do?",
                    "Is stomach flu dangerous for kids?",
                    "How to treat gastroenteritis in children?"
                ],
                "completion": "Children with gastroenteritis should drink fluids to prevent dehydration. Avoid sugary drinks and give oral rehydration solutions. Seek medical help if there is blood in stool, high fever, or persistent vomiting."
            }
        ]
    },
    {
        "name": "Gastritis",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have upper stomach pain and nausea. Could it be gastritis?",
                    "What are the symptoms of gastritis?",
                    "How to manage gastritis?"
                ],
                "completion": "Gastritis is inflammation of the stomach lining, causing pain, bloating, and nausea. Avoid irritants like alcohol and spicy food. See a doctor for persistent symptoms."
            }
        ]
    },
    {
        "name": "Gastroesophageal Reflux Disease (GERD)",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have heartburn after meals. Could it be acid reflux?",
                    "What are GERD symptoms?",
                    "How to relieve acid reflux?"
                ],
                "completion": "GERD causes heartburn, regurgitation, and sometimes cough. Avoid large meals, elevate your head while sleeping, and reduce trigger foods. Persistent symptoms should be evaluated by a doctor."
            }
        ]
    },
    {
        "name": "Irritable Bowel Syndrome (IBS)",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have alternating diarrhea and constipation with abdominal pain.",
                    "What are the symptoms of IBS?",
                    "How to manage irritable bowel syndrome?"
                ],
                "completion": "IBS causes abdominal discomfort, bloating, and changes in bowel habits. Stress reduction, dietary changes, and medical guidance help manage symptoms."
            }
        ]
    },
    {
        "name": "Constipation",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I haven't had a bowel movement in several days. What can I do?",
                    "What causes constipation?",
                    "How to relieve constipation?"
                ],
                "completion": "Constipation can be relieved by drinking water, eating fiber-rich foods, and exercising. Persistent constipation may require medical evaluation."
            },
            {
                "group": "Elderly",
                "prompts": [
                    "My elderly parent is constipated often. Is this normal?",
                    "How can constipation in seniors be treated?",
                    "What causes constipation in older adults?"
                ],
                "completion": "Constipation is common in older adults due to diet, inactivity, or medications. Increase fluids, fiber, and activity. Consult a doctor if it persists."
            }
        ]
    },
    {
        "name": "Type 2 Diabetes",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I feel constantly thirsty and tired. Could this be diabetes?",
                    "What are the early symptoms of type 2 diabetes?",
                    "How can I manage type 2 diabetes?"
                ],
                "completion": "Type 2 diabetes can cause thirst, fatigue, and frequent urination. Management involves healthy eating, regular exercise, and medication under medical supervision."
            }
        ]
    },
    {
        "name": "Hypothyroidism",
        "variations": [
            {
                "group": "Adult Female",
                "prompts": [
                    "I feel tired, have weight gain, and my hair is thinning. Could this be thyroid related?",
                    "What are hypothyroidism symptoms?",
                    "How is hypothyroidism treated?"
                ],
                "completion": "Hypothyroidism slows body processes, causing fatigue, weight gain, and hair thinning. It is treated with thyroid hormone replacement prescribed by a doctor."
            }
        ]
    },
    {
        "name": "Hyperthyroidism",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have rapid heartbeat, weight loss, and anxiety. Could this be thyroid disease?",
                    "What are hyperthyroidism symptoms?",
                    "How is hyperthyroidism treated?"
                ],
                "completion": "Hyperthyroidism speeds up body processes, leading to rapid heartbeat, weight loss, and irritability. It requires medical evaluation and treatment."
            }
        ]
    },
    {
        "name": "Urinary Tract Infection (UTI)",
        "variations": [
            {
                "group": "Adult Female",
                "prompts": [
                    "I have burning when urinating and a frequent urge to go. Could it be a UTI?",
                    "What are the symptoms of a urinary tract infection?",
                    "How are UTIs treated?"
                ],
                "completion": "UTIs cause burning during urination, urgency, and pelvic discomfort. Drink water, avoid irritants, and see a doctor for antibiotics."
            },
            {
                "group": "Elderly",
                "prompts": [
                    "My elderly mother is confused and has urinary changes. Could it be a UTI?",
                    "How do UTIs present in seniors?",
                    "When should an elderly person with a UTI see a doctor?"
                ],
                "completion": "In seniors, UTIs may cause confusion and weakness rather than typical symptoms. Seek medical care promptly."
            }
        ]
    },
    {
        "name": "Kidney Stones",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have severe back pain and blood in my urine. Could it be kidney stones?",
                    "What are the symptoms of kidney stones?",
                    "How are kidney stones treated?"
                ],
                "completion": "Kidney stones cause sharp flank pain, blood in urine, and nausea. Small stones may pass naturally with hydration; larger stones may require medical intervention."
            }
        ]
    },
        {
        "name": "Polycystic Ovary Syndrome (PCOS)",
        "variations": [
            {
                "group": "Adult Female",
                "prompts": [
                    "I have irregular periods and acne. Could this be PCOS?",
                    "What are the symptoms of PCOS?",
                    "How is PCOS managed?"
                ],
                "completion": "PCOS can cause irregular periods, acne, weight gain, and excess hair growth. Management includes lifestyle changes, hormonal treatments, and medical guidance."
            }
        ]
    },
    {
        "name": "Endometriosis",
        "variations": [
            {
                "group": "Adult Female",
                "prompts": [
                    "I have severe cramps during my period. Could it be endometriosis?",
                    "What are the symptoms of endometriosis?",
                    "How is endometriosis treated?"
                ],
                "completion": "Endometriosis causes pelvic pain, heavy periods, and sometimes infertility. Diagnosis requires medical evaluation and treatment can involve medication or surgery."
            }
        ]
    },
    {
        "name": "Benign Prostatic Hyperplasia (BPH)",
        "variations": [
            {
                "group": "Adult Male",
                "prompts": [
                    "I have trouble starting urination and a weak stream. Could this be prostate enlargement?",
                    "What are the symptoms of BPH?",
                    "How is prostate enlargement treated?"
                ],
                "completion": "BPH causes urinary hesitancy, weak stream, and frequent urination in older men. Treatment options range from medication to surgery based on severity."
            }
        ]
    },
    {
        "name": "Prostate Cancer",
        "variations": [
            {
                "group": "Adult Male",
                "prompts": [
                    "I have difficulty urinating and pelvic discomfort. Could this be prostate cancer?",
                    "What are the signs of prostate cancer?",
                    "How is prostate cancer diagnosed?"
                ],
                "completion": "Prostate cancer may cause urinary issues or be asymptomatic in early stages. Screening and medical evaluation are necessary for diagnosis and treatment planning."
            }
        ]
    },
    {
        "name": "Pregnancy — Morning Sickness",
        "variations": [
            {
                "group": "Pregnant Female",
                "prompts": [
                    "I feel nauseous every morning during early pregnancy. Is this normal?",
                    "What causes morning sickness?",
                    "How to manage nausea during pregnancy?"
                ],
                "completion": "Morning sickness is common in early pregnancy and involves nausea and sometimes vomiting. Eat small, frequent meals, stay hydrated, and rest. Severe symptoms should be evaluated by a doctor."
            }
        ]
    },
    {
        "name": "Pregnancy — Gestational Diabetes",
        "variations": [
            {
                "group": "Pregnant Female",
                "prompts": [
                    "I was diagnosed with gestational diabetes. What does it mean?",
                    "What are the risks of gestational diabetes?",
                    "How is gestational diabetes managed?"
                ],
                "completion": "Gestational diabetes is high blood sugar during pregnancy. Management includes dietary changes, regular monitoring, and sometimes insulin, under medical supervision."
            }
        ]
    },
    {
        "name": "Eczema",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have dry, itchy skin patches. Could it be eczema?",
                    "What are eczema symptoms?",
                    "How to manage eczema flare-ups?"
                ],
                "completion": "Eczema causes itchy, inflamed skin. Moisturizing regularly, avoiding triggers, and using doctor-recommended treatments can help control symptoms."
            },
            {
                "group": "Child",
                "prompts": [
                    "My child has red, itchy skin behind the knees. Could it be eczema?",
                    "What causes eczema in kids?",
                    "How to treat childhood eczema?"
                ],
                "completion": "Childhood eczema causes dry, itchy patches often in skin folds. Use fragrance-free moisturizers and avoid irritants. Seek medical advice for severe or persistent flare-ups."
            }
        ]
    },
    {
        "name": "Psoriasis",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have thick, scaly skin patches on my elbows. Could it be psoriasis?",
                    "What are psoriasis symptoms?",
                    "How is psoriasis treated?"
                ],
                "completion": "Psoriasis is a chronic skin condition causing red, scaly patches. Treatment includes moisturizers, topical medicines, and sometimes light therapy or oral medication."
            }
        ]
    },
    {
        "name": "Acne",
        "variations": [
            {
                "group": "Teenager",
                "prompts": [
                    "I have pimples on my face and back. Is this normal?",
                    "What causes acne in teenagers?",
                    "How to manage acne?"
                ],
                "completion": "Acne is common in teenagers due to hormonal changes. Wash gently, avoid picking pimples, and use over-the-counter treatments. Severe acne may require a dermatologist."
            },
            {
                "group": "Adult Female",
                "prompts": [
                    "I get acne breakouts around my period. Is this hormonal?",
                    "Why do I have adult acne?",
                    "How to treat hormonal acne?"
                ],
                "completion": "Adult acne can be hormonal and linked to menstrual cycles. Treatment may involve topical medications, oral therapies, or hormonal management prescribed by a doctor."
            }
        ]
    },
    {
        "name": "Osteoarthritis",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have joint pain and stiffness. Could it be arthritis?",
                    "What are osteoarthritis symptoms?",
                    "How is osteoarthritis managed?"
                ],
                "completion": "Osteoarthritis causes joint pain, stiffness, and reduced flexibility. Maintaining a healthy weight, exercising, and using pain relief as advised by a doctor can help."
            }
        ]
    },
    {
        "name": "Rheumatoid Arthritis",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "My joints are swollen and stiff in the morning. Could it be rheumatoid arthritis?",
                    "What are the symptoms of rheumatoid arthritis?",
                    "How is rheumatoid arthritis treated?"
                ],
                "completion": "Rheumatoid arthritis is an autoimmune disease causing joint inflammation, swelling, and stiffness. Early medical treatment can slow disease progression."
            }
        ]
    },
        {
        "name": "Migraine",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have severe headaches with light sensitivity. Could it be a migraine?",
                    "What are migraine symptoms?",
                    "How are migraines treated?"
                ],
                "completion": "Migraines cause intense headaches often with nausea and light sensitivity. Resting in a dark room, staying hydrated, and prescribed medications can help manage symptoms."
            }
        ]
    },
    {
        "name": "Epilepsy",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I had a seizure for the first time. Could it be epilepsy?",
                    "What causes epilepsy?",
                    "How is epilepsy treated?"
                ],
                "completion": "Epilepsy is a neurological disorder that causes seizures. Diagnosis requires medical evaluation, and treatment usually involves anti-seizure medications."
            }
        ]
    },
    {
        "name": "Stroke",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have sudden weakness on one side and slurred speech. Could it be a stroke?",
                    "What are stroke symptoms?",
                    "What should I do if I suspect a stroke?"
                ],
                "completion": "Stroke symptoms include sudden weakness, facial drooping, and speech difficulty. This is a medical emergency — call emergency services immediately."
            }
        ]
    },
    {
        "name": "Parkinson’s Disease",
        "variations": [
            {
                "group": "Elderly",
                "prompts": [
                    "I have tremors and slow movement. Could it be Parkinson’s?",
                    "What are the symptoms of Parkinson’s disease?",
                    "How is Parkinson’s managed?"
                ],
                "completion": "Parkinson’s disease causes tremors, stiffness, and slow movements. Treatment includes medication, therapy, and lifestyle changes under a doctor’s care."
            }
        ]
    },
    {
        "name": "Depression",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I feel sad and hopeless most of the time. Could I be depressed?",
                    "What are the symptoms of depression?",
                    "How is depression treated?"
                ],
                "completion": "Depression is a mental health condition with persistent sadness, fatigue, and loss of interest. Treatment involves therapy, lifestyle support, and sometimes medication."
            }
        ]
    },
    {
        "name": "Generalized Anxiety Disorder",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I feel anxious and worried all the time. Is this normal?",
                    "What are the signs of generalized anxiety disorder?",
                    "How is anxiety treated?"
                ],
                "completion": "Generalized anxiety disorder causes excessive, ongoing worry. Management includes therapy, relaxation techniques, and sometimes prescribed medication."
            }
        ]
    },
    {
        "name": "Post-Traumatic Stress Disorder (PTSD)",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I keep having flashbacks after a traumatic event. Could it be PTSD?",
                    "What are PTSD symptoms?",
                    "How is PTSD treated?"
                ],
                "completion": "PTSD can follow trauma and cause flashbacks, nightmares, and anxiety. Treatment includes therapy and support from mental health professionals."
            }
        ]
    },
    {
        "name": "Seasonal Allergies (Hay Fever)",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I sneeze a lot and have itchy eyes every spring. Could it be allergies?",
                    "What are the symptoms of hay fever?",
                    "How to manage seasonal allergies?"
                ],
                "completion": "Seasonal allergies cause sneezing, itchy eyes, and congestion. Antihistamines and avoiding triggers can help."
            }
        ]
    },
    {
        "name": "Asthma",
        "variations": [
            {
                "group": "Child",
                "prompts": [
                    "My child wheezes and coughs when running. Could it be asthma?",
                    "What are asthma symptoms in children?",
                    "How is asthma managed?"
                ],
                "completion": "Asthma causes wheezing, coughing, and shortness of breath. Management includes avoiding triggers and using prescribed inhalers."
            }
        ]
    },
    {
        "name": "HIV/AIDS",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I had unprotected sex and now feel unwell. Could it be HIV?",
                    "What are the symptoms of HIV?",
                    "How is HIV treated?"
                ],
                "completion": "HIV weakens the immune system and can progress to AIDS. Early testing and antiretroviral treatment greatly improve outcomes."
            }
        ]
    },
    {
        "name": "Tuberculosis (TB)",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have a persistent cough for weeks and night sweats. Could it be TB?",
                    "What are tuberculosis symptoms?",
                    "How is TB treated?"
                ],
                "completion": "TB is a bacterial lung infection with a long cough, fever, and weight loss. It requires medical diagnosis and prolonged antibiotic treatment."
            }
        ]
    },
    {
        "name": "COVID-19",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I lost my sense of taste and smell. Could it be COVID?",
                    "What are COVID-19 symptoms?",
                    "How is COVID-19 treated?"
                ],
                "completion": "COVID-19 can cause fever, cough, loss of taste/smell, and fatigue. Isolate, get tested, and follow public health guidance. Seek urgent care for breathing problems."
            }
        ]
    },
    {
        "name": "Lupus",
        "variations": [
            {
                "group": "Adult Female",
                "prompts": [
                    "I have joint pain, rashes, and fatigue. Could it be lupus?",
                    "What are lupus symptoms?",
                    "How is lupus treated?"
                ],
                "completion": "Lupus is an autoimmune disease affecting joints, skin, and organs. Treatment involves medication and lifestyle management under medical supervision."
            }
        ]
    },
    # --- Chunk 5: Extra Common Conditions ---

    # --- Respiratory & ENT ---
    {
        "name": "Sinusitis",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have pressure and pain in my face, plus a stuffy nose. Is this a sinus infection?",
                    "What are the symptoms of sinusitis?",
                    "How do you treat a sinus infection?"
                ],
                "completion": "Sinusitis involves inflammation of the sinuses, causing facial pain, pressure, and nasal congestion. Home care includes saline rinses and rest. See a doctor if symptoms are severe or persist, as antibiotics may be needed."
            }
        ]
    },
    {
        "name": "Bronchitis",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have a deep, hacking cough with mucus after a cold. Could it be bronchitis?",
                    "What are the signs of acute bronchitis?",
                    "How is bronchitis treated?"
                ],
                "completion": "Acute bronchitis is chest inflammation causing a persistent cough and mucus. It's usually viral. Treatment involves rest, fluids, and sometimes an inhaler. A doctor should be consulted if you have a high fever or trouble breathing."
            }
        ]
    },
    {
        "name": "Otitis Media (Middle Ear Infection)",
        "variations": [
            {
                "group": "Child",
                "prompts": [
                    "My toddler is pulling at their ear and has a fever. Could it be an ear infection?",
                    "What are symptoms of an ear infection in a baby?",
                    "How are childhood ear infections treated?"
                ],
                "completion": "Middle ear infections (otitis media) are common in children, causing ear pain, fever, and irritability. It is essential to see a pediatrician for diagnosis, as antibiotic treatment may be required."
            }
        ]
    },

    # --- Digestive & Gastrointestinal ---
    {
        "name": "Gastroesophageal Reflux Disease (GERD)",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I get painful heartburn multiple times a week. Could it be GERD?",
                    "What are the symptoms of GERD?",
                    "How is chronic acid reflux managed?"
                ],
                "completion": "GERD is a chronic condition causing frequent acid reflux and heartburn. Management includes diet changes and medication. A doctor can provide a diagnosis and treatment plan to prevent complications."
            }
        ]
    },
    {
        "name": "Irritable Bowel Syndrome (IBS)",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have chronic bloating, gas, and my digestion is unpredictable. Could it be IBS?",
                    "What are the symptoms of IBS?",
                    "How is irritable bowel syndrome treated?"
                ],
                "completion": "IBS is a common disorder causing cramping, abdominal pain, bloating, gas, diarrhea, and constipation. A doctor can help diagnose it and suggest dietary and lifestyle changes for management."
            }
        ]
    },

    # --- Endocrine & Metabolic ---
    {
        "name": "Polycystic Ovary Syndrome (PCOS)",
        "variations": [
            {
                "group": "Adult Female",
                "prompts": [
                    "I have very irregular periods and bad acne. Could it be PCOS?",
                    "What are the signs of PCOS?",
                    "How is PCOS diagnosed and managed?"
                ],
                "completion": "PCOS is a hormonal disorder causing irregular periods and elevated androgen levels. A gynecologist or endocrinologist can diagnose it and recommend lifestyle changes or medication for management."
            }
        ]
    },
    {
        "name": "Gout",
        "variations": [
            {
                "group": "Adult Male",
                "prompts": [
                    "I have sudden, excruciating pain in my big toe. Could it be gout?",
                    "What are gout symptoms?",
                    "How is gout treated?"
                ],
                "completion": "Gout is a form of arthritis causing sudden, severe attacks of pain and swelling in a joint, often the big toe. It requires medical diagnosis and treatment with medication to manage attacks and lower uric acid levels."
            }
        ]
    },
    
    # --- Musculoskeletal ---
    {
        "name": "Rheumatoid Arthritis",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have stiff, swollen, and painful joints, especially in the morning. Could this be rheumatoid arthritis?",
                    "What are the symptoms of rheumatoid arthritis?",
                    "How is RA treated?"
                ],
                "completion": "Rheumatoid arthritis is an autoimmune disorder where the immune system attacks the joints, causing inflammation and pain. Early diagnosis and treatment by a rheumatologist are crucial to slow disease progression."
            }
        ]
    },
    {
        "name": "Osteoporosis",
        "variations": [
            {
                "group": "Elderly Female",
                "prompts": [
                    "I'm an older woman and I broke a bone from a simple fall. Could I have osteoporosis?",
                    "What are the signs of osteoporosis?",
                    "How is bone density loss treated?"
                ],
                "completion": "Osteoporosis weakens bones, making them fragile and more likely to break. It's common in older women. A doctor can order a bone density scan for diagnosis and prescribe treatments to strengthen bones."
            }
        ]
    },

    # --- Skin Conditions ---
    {
        "name": "Shingles (Herpes Zoster)",
        "variations": [
            {
                "group": "Elderly",
                "prompts": [
                    "I have a painful, blistering rash on one side of my torso. Is this shingles?",
                    "What are the symptoms of shingles?",
                    "What should I do if I think I have shingles?"
                ],
                "completion": "Shingles is a viral infection that causes a painful rash, usually in a single stripe on one side of the body. It's crucial to see a doctor immediately for antiviral medication to reduce pain and complications."
            }
        ]
    },
    
    # --- Infectious Diseases ---
    {
        "name": "Chickenpox (Varicella)",
        "variations": [
            {
                "group": "Child",
                "prompts": [
                    "My child has an itchy rash that looks like blisters all over. Is it chickenpox?",
                    "What are the symptoms of chickenpox?",
                    "How do I care for a child with chickenpox?"
                ],
                "completion": "Chickenpox causes an itchy rash with fluid-filled blisters. While usually mild, it's very contagious. Consult a pediatrician for diagnosis and advice on comfort measures and preventing complications."
            }
        ]
    },
    {
            "name": "Common Cold",
            "variations": [
                {
                    "group": "Adult (18-65)",
                    "prompts": [
                        "I have a runny nose, sneezing, and a sore throat. What could it be?",
                        "What are the symptoms of the common cold for an adult?",
                        "How do you treat a common cold?",
                        "I've been sneezing all day and my nose is stuffy. Is this a cold?",
                        "My throat hurts and I have a headache. Could this be a cold?",
                        "I feel congested and have been coughing. What should I do?",
                        "I have a mild fever with runny nose and body aches."
                    ],
                    "completion": "Based on symptoms like runny nose, sneezing, and sore throat, this appears to be a common cold. For adults, management includes rest, staying hydrated (8-10 glasses of water daily), using over-the-counter pain relievers like acetaminophen or ibuprofen for aches, and throat lozenges for sore throat. Symptoms typically resolve in 7-10 days. Seek medical attention if symptoms worsen after 3 days, fever exceeds 101.3°F (38.5°C), or you develop severe headache or sinus pain."
                },
                {
                    "group": "Infant (0-2 years)",
                    "prompts": [
                        "My 6-month-old baby has a stuffy nose and is sneezing frequently.",
                        "What should I do if my infant has cold symptoms?",
                        "My baby is congested and seems uncomfortable. What can I do?",
                        "How to help a 1-year-old with a runny nose?",
                        "My toddler has been sneezing and has a clear runny nose.",
                        "My 8-month-old is having trouble feeding due to congestion."
                    ],
                    "completion": "For infants with cold symptoms like congestion and sneezing, use saline nasal drops and a bulb syringe to clear nasal passages. Ensure adequate hydration through breast milk or formula. Use a cool-mist humidifier in the baby's room. NEVER give over-the-counter cold medications to children under 2 years. Contact your pediatrician immediately if the baby has difficulty breathing, refuses to eat, has a fever over 100.4°F (38°C), or shows signs of dehydration."
                },
                {
                    "group": "Elderly (65+)",
                    "prompts": [
                        "I'm 70 years old and have cold symptoms. Should I be concerned?",
                        "What precautions should elderly people take with a cold?",
                        "I'm a senior citizen with a runny nose and cough. What should I do?"
                    ],
                    "completion": "For seniors, cold symptoms require closer monitoring due to increased risk of complications like pneumonia. While managing symptoms with rest and hydration, watch for signs of bacterial infection: yellow/green mucus, persistent cough, chest pain, or breathing difficulties. Contact your healthcare provider if symptoms don't improve within 7 days or if you have underlying conditions like COPD, heart disease, or diabetes. Consider getting a flu shot annually to prevent more serious respiratory infections."
                }
            ]
        },
        {
            "name": "Influenza (Flu)",
            "variations": [
                {
                    "group": "Adult (18-65)",
                    "prompts": [
                        "I have high fever, body aches, and feel extremely tired.",
                        "What are flu symptoms versus a cold?",
                        "I have chills, headache, and muscle pain all over.",
                        "How do you treat the flu?",
                        "I feel terrible with fever and aches. Could this be influenza?",
                        "I have a dry cough with high fever and feel exhausted."
                    ],
                    "completion": "High fever, severe body aches, chills, and extreme fatigue suggest influenza rather than a common cold. Treatment includes rest, plenty of fluids, and over-the-counter fever reducers. Antiviral medications like Tamiflu are most effective when started within 48 hours of symptom onset. Most healthy adults recover in 7-10 days. Seek medical attention if you have difficulty breathing, persistent high fever, chest pain, or if you're in a high-risk group (over 65, pregnant, or have chronic conditions)."
                },
                {
                    "group": "High-Risk Adults (Chronic Conditions)",
                    "prompts": [
                        "I have diabetes and think I have the flu. Should I be worried?",
                        "How does flu affect people with heart disease?",
                        "I have COPD and flu symptoms. What should I do?"
                    ],
                    "completion": "Adults with chronic conditions like diabetes, heart disease, or COPD are at high risk for flu complications including pneumonia and hospitalization. Contact your healthcare provider immediately for flu symptoms to discuss antiviral medications. Monitor blood sugar closely if diabetic, as illness can affect glucose control. Watch for warning signs: difficulty breathing, chest pain, persistent vomiting, or worsening of underlying conditions. Annual flu vaccination is especially important for high-risk individuals."
                }
            ]
        },
        {
            "name": "Pneumonia",
            "variations": [
                {
                    "group": "Adult (18-65)",
                    "prompts": [
                        "I have a high fever, cough with yellow phlegm, and chest pain.",
                        "What are pneumonia symptoms?",
                        "I'm having trouble breathing and feel very sick.",
                        "How serious is pneumonia?",
                        "I have chills, fever, and a productive cough.",
                        "My chest hurts when I breathe deeply and I'm coughing up mucus."
                    ],
                    "completion": "High fever, productive cough with colored sputum, chest pain, and breathing difficulties suggest pneumonia, a serious infection requiring medical attention. Pneumonia needs prompt evaluation and often antibiotic treatment. Seek immediate medical care, especially if you have difficulty breathing, chest pain, high fever (>101°F), or feel severely ill. Treatment may include antibiotics, rest, increased fluid intake, and potentially hospitalization for severe cases. Complete the full course of prescribed antibiotics even if feeling better."
                },
                {
                    "group": "Elderly (65+)",
                    "prompts": [
                        "I'm elderly and have been feeling weak with a mild cough.",
                        "How does pneumonia present in seniors?",
                        "I'm 75 and not feeling well, but don't have much fever.",
                        "My elderly parent seems confused and weak lately."
                    ],
                    "completion": "Pneumonia in elderly adults can present subtly without typical symptoms. Instead of high fever and obvious respiratory symptoms, seniors may experience confusion, weakness, loss of appetite, or falls. Even a mild cough with general malaise warrants medical evaluation in this age group. Pneumonia is particularly dangerous for adults over 65 due to weakened immune systems and often requires hospitalization. Seek immediate medical attention for any respiratory symptoms or unexplained decline in elderly individuals."
                }
            ]
        },
        {
            "name": "Asthma",
            "variations": [
                {
                    "group": "Children (5-18 years)",
                    "prompts": [
                        "My child wheezes and has trouble breathing, especially at night.",
                        "What are asthma symptoms in kids?",
                        "My child coughs a lot during exercise and gets short of breath.",
                        "How do you manage childhood asthma?",
                        "My kid's breathing sounds whistling and they complain of chest tightness."
                    ],
                    "completion": "Wheezing, nighttime cough, exercise-induced breathing difficulties, and chest tightness in children suggest asthma. This requires medical evaluation for proper diagnosis and treatment plan. Management includes identifying and avoiding triggers (allergens, irritants), using prescribed bronchodilator inhalers for symptoms, and potentially daily controller medications. Ensure the child and family know proper inhaler technique. Create an asthma action plan with your pediatrician. Seek immediate care for severe breathing difficulty, inability to speak in full sentences, or blue lips/fingernails."
                },
                {
                    "group": "Adult (18-65)",
                    "prompts": [
                        "I wheeze and get short of breath with exercise or exposure to dust.",
                        "Can adults develop asthma?",
                        "I have a persistent cough that's worse at night.",
                        "What triggers adult-onset asthma?",
                        "I have chest tightness when I'm around cats or pollen."
                    ],
                    "completion": "Adult-onset asthma can develop due to occupational exposures, infections, or hormonal changes. Symptoms include wheezing, shortness of breath, chest tightness, and persistent cough, especially at night or with exercise. Avoid known triggers, use prescribed rescue inhalers for acute symptoms, and follow controller medication regimens as prescribed. Adult asthma requires ongoing medical management - consult a pulmonologist for comprehensive evaluation, especially if symptoms interfere with daily activities or sleep."
                }
            ]
        },
        
        # CARDIOVASCULAR SYSTEM
        {
            "name": "Hypertension (High Blood Pressure)",
            "variations": [
                {
                    "group": "Adult (35-65)",
                    "prompts": [
                        "I've been having headaches and my blood pressure readings are high.",
                        "What are symptoms of high blood pressure?",
                        "How do you manage hypertension naturally?",
                        "I feel dizzy and have been getting headaches frequently.",
                        "My doctor said my blood pressure is elevated. What should I do?",
                        "I have no symptoms but my BP is 150/90. Is this serious?"
                    ],
                    "completion": "High blood pressure often has no symptoms, earning it the nickname 'silent killer.' However, some people experience headaches, dizziness, or fatigue. If diagnosed with hypertension, lifestyle modifications include reducing sodium intake (under 2300mg daily), regular exercise (30 minutes most days), maintaining healthy weight, limiting alcohol, and managing stress. Monitor blood pressure regularly at home. Follow up with your healthcare provider for medication management if lifestyle changes aren't sufficient to reach target blood pressure."
                },
                {
                    "group": "African American Adults",
                    "prompts": [
                        "As an African American, should I be more concerned about high blood pressure?",
                        "How does hypertension affect Black Americans differently?",
                        "What are the risks of high blood pressure in the Black community?"
                    ],
                    "completion": "African Americans have a higher prevalence of hypertension and develop it at younger ages, often with more severe complications. This population faces increased risk of stroke, heart disease, and kidney disease from high blood pressure. More aggressive monitoring and treatment may be necessary, with earlier initiation of medication. Dietary approaches emphasizing potassium-rich foods, reduced sodium, and the DASH diet are particularly beneficial. Regular blood pressure monitoring and close collaboration with healthcare providers is essential for optimal management."
                }
            ]
        },
        {
            "name": "Chest Pain (Non-Cardiac)",
            "variations": [
                {
                    "group": "Adult (25-55)",
                    "prompts": [
                        "I have chest pain but my heart was checked and is fine.",
                        "What causes chest pain that's not heart-related?",
                        "I have sharp chest pain when I breathe deeply.",
                        "My chest hurts but it's not a heart attack. What could it be?",
                        "I have burning chest pain after eating."
                    ],
                    "completion": "Chest pain with normal cardiac evaluation can have several causes: acid reflux (burning pain after eating), muscle strain (sharp pain with movement), anxiety (associated with stress/panic), or costochondritis (chest wall inflammation). Treatment depends on the cause - antacids for reflux, anti-inflammatory medications for muscle/joint pain, stress management for anxiety-related pain. However, any new or severe chest pain should be evaluated medically to rule out serious causes."
                }
            ]
        },
        
        # GASTROINTESTINAL SYSTEM
        {
            "name": "Gastroenteritis (Stomach Flu)",
            "variations": [
                {
                    "group": "Adult (18-65)",
                    "prompts": [
                        "I have nausea, vomiting, and diarrhea. What could this be?",
                        "What should I do for stomach flu symptoms?",
                        "I can't keep food down and have been having diarrhea.",
                        "How do you treat gastroenteritis?",
                        "I have stomach cramps and frequent loose stools.",
                        "I feel nauseous and have been vomiting for 12 hours.",
                        "I have watery diarrhea and feel dehydrated."
                    ],
                    "completion": "Symptoms of nausea, vomiting, and diarrhea suggest gastroenteritis (stomach flu). Focus on preventing dehydration by sipping clear fluids like water, clear broths, or oral rehydration solutions. Start with the BRAT diet (bananas, rice, applesauce, toast) when you can tolerate food. Avoid dairy, fatty foods, and caffeine. Rest and gradual return to normal diet as symptoms improve. Seek medical care if you have signs of severe dehydration, blood in vomit/stool, high fever (>101.5°F), or symptoms persist beyond 3-4 days."
                },
                {
                    "group": "Children (2-12 years)",
                    "prompts": [
                        "My 5-year-old has been throwing up and has diarrhea.",
                        "What should I give my child for stomach flu?",
                        "My kid can't keep anything down and has stomach upset.",
                        "My child has been vomiting and won't eat or drink."
                    ],
                    "completion": "For children with gastroenteritis, the primary concern is preventing dehydration. Offer small, frequent sips of clear fluids like water, diluted fruit juice, or pediatric electrolyte solutions. Avoid anti-diarrheal medications in children. Once vomiting subsides, introduce bland foods gradually. Monitor for dehydration signs: dry mouth, no tears when crying, decreased urination, or lethargy. Contact your pediatrician immediately if the child shows signs of dehydration, has blood in vomit/stool, or high fever."
                }
            ]
        },
        {
            "name": "GERD (Acid Reflux)",
            "variations": [
                {
                    "group": "Adult (30-65)",
                    "prompts": [
                        "I have burning in my chest after eating, especially at night.",
                        "What are symptoms of acid reflux?",
                        "I get heartburn frequently and sometimes taste acid in my mouth.",
                        "How do you treat GERD?",
                        "I have chest burning that gets worse when I lie down.",
                        "I wake up with acid in my throat and a sour taste.",
                        "I have chronic heartburn that affects my sleep."
                    ],
                    "completion": "Burning chest pain after eating, especially when lying down, with acid taste suggests GERD (acid reflux). Management includes eating smaller meals, avoiding trigger foods (spicy, fatty, acidic foods), not eating 3 hours before bedtime, elevating the head of your bed 6-8 inches, and maintaining healthy weight. Over-the-counter antacids or H2 blockers can provide relief. If symptoms occur more than twice weekly, persist despite lifestyle changes, or you experience difficulty swallowing, consult a gastroenterologist for evaluation and potential prescription treatment."
                },
                {
                    "group": "Pregnant Women",
                    "prompts": [
                        "I'm pregnant and have terrible heartburn.",
                        "Is acid reflux normal during pregnancy?",
                        "What's safe for heartburn when you're expecting?",
                        "I'm in my third trimester with severe heartburn."
                    ],
                    "completion": "Heartburn is very common during pregnancy, especially in the second and third trimesters, due to hormonal changes and growing uterus pressure. Safe treatments include eating smaller, frequent meals, avoiding trigger foods, not lying down immediately after eating, and sleeping with head elevated. Calcium carbonate antacids (Tums) are generally safe during pregnancy. Avoid aspirin-containing antacids. If symptoms are severe or interfere with eating/sleeping, consult your obstetrician about safe prescription options."
                }
            ]
        },
        {
            "name": "Irritable Bowel Syndrome (IBS)",
            "variations": [
                {
                    "group": "Adult (20-50)",
                    "prompts": [
                        "I have alternating diarrhea and constipation with abdominal pain.",
                        "What are IBS symptoms?",
                        "My stomach hurts and my bowel movements are unpredictable.",
                        "How do you manage irritable bowel syndrome?",
                        "I have bloating and cramping that comes and goes.",
                        "I have urgent bowel movements and stomach pain after eating.",
                        "My digestive system is very sensitive to stress and certain foods."
                    ],
                    "completion": "Alternating bowel habits with abdominal pain, bloating, and cramping suggest irritable bowel syndrome (IBS). Management includes identifying food triggers through elimination diet, increasing fiber gradually, staying hydrated, regular exercise, and stress management. Common triggers include high-fat foods, dairy, artificial sweeteners, and high-FODMAP foods. Keep a food and symptom diary to identify patterns. If symptoms are severe, include blood in stool, or cause significant weight loss, consult a gastroenterologist to rule out other conditions."
                },
                {
                    "group": "Women (20-40)",
                    "prompts": [
                        "My IBS symptoms get worse during my menstrual cycle.",
                        "How do hormones affect IBS in women?",
                        "I have more stomach problems around my period."
                    ],
                    "completion": "Many women with IBS notice symptom flares during menstruation due to hormonal fluctuations. Estrogen and progesterone changes can affect gut motility and sensitivity. Track symptoms in relation to your menstrual cycle to identify patterns. Management may include adjusting diet and stress management techniques around your cycle, and potentially hormonal treatments in severe cases. Discuss hormonal patterns with your gastroenterologist for personalized treatment strategies."
                }
            ]
        },
        {
            "name": "Food Poisoning",
            "variations": [
                {
                    "group": "Adult (18-65)",
                    "prompts": [
                        "I ate at a restaurant yesterday and now have severe nausea and diarrhea.",
                        "What are food poisoning symptoms?",
                        "I have stomach cramps and have been vomiting since eating seafood.",
                        "How do you treat food poisoning?",
                        "I feel sick after eating and have been having diarrhea for hours.",
                        "I ate something and within hours felt terrible with stomach pain."
                    ],
                    "completion": "Sudden onset of nausea, vomiting, diarrhea, and stomach cramps within hours of eating suggests food poisoning. Focus on preventing dehydration by sipping clear fluids frequently - water, clear broths, or oral rehydration solutions. Avoid solid foods until vomiting stops, then gradually introduce bland foods. Rest and avoid dairy, fatty foods, alcohol, and caffeine. Most food poisoning resolves within 3-7 days. Seek medical care if you develop signs of severe dehydration, high fever (>101.5°F), blood in vomit/stool, or severe abdominal pain."
                }
            ]
        },
        
        # MUSCULOSKELETAL SYSTEM
        {
            "name": "Lower Back Pain",
            "variations": [
                {
                    "group": "Adult (25-55)",
                    "prompts": [
                        "I lifted something heavy and now my lower back is in severe pain.",
                        "What should I do for acute back pain?",
                        "My back went out and I can barely move.",
                        "How do you treat a pulled back muscle?",
                        "I have sharp pain in my lower back that started suddenly.",
                        "I can't stand up straight because of back pain.",
                        "My lower back aches constantly and stiffens up."
                    ],
                    "completion": "Acute lower back pain from lifting often involves muscle strain or sprain. Initial treatment follows the principle of controlled activity rather than complete bed rest. Apply ice for the first 24-48 hours, then alternate with heat. Take anti-inflammatory medications like ibuprofen as directed. Gentle movement and stretching as tolerated helps recovery. Most acute back pain improves within a few days to weeks. Seek immediate medical attention if you experience leg weakness, numbness, loss of bladder/bowel control, or severe radiating pain down the leg."
                },
                {
                    "group": "Office Workers (25-55)",
                    "prompts": [
                        "I sit at a desk all day and have chronic lower back pain.",
                        "How does sitting affect back pain?",
                        "I have back pain from poor posture at work."
                    ],
                    "completion": "Prolonged sitting with poor posture commonly causes lower back pain in office workers. Prevention and treatment include ergonomic workspace setup, taking regular breaks to stand/walk (every 30-60 minutes), strengthening core muscles, and improving posture. Use a supportive chair with lumbar support, keep feet flat on floor, and position computer screen at eye level. If pain persists, consider physical therapy for posture training and strengthening exercises."
                }
            ]
        },
        {
            "name": "Osteoarthritis",
            "variations": [
                {
                    "group": "Adult (45-75)",
                    "prompts": [
                        "My knees are stiff and painful, especially in the morning.",
                        "What are early signs of arthritis?",
                        "I have joint pain that gets worse with activity.",
                        "How do you treat arthritis naturally?",
                        "My fingers are stiff and hurt when I grip things.",
                        "My joints ache when the weather changes.",
                        "I have trouble going up stairs because my knees hurt."
                    ],
                    "completion": "Morning stiffness and joint pain that worsens with activity suggests osteoarthritis, especially in weight-bearing joints like knees. Management includes low-impact exercise (swimming, walking), weight management to reduce joint stress, application of heat/cold therapy, and over-the-counter anti-inflammatory medications. Physical therapy can help maintain joint function and strength. If pain significantly limits daily activities or doesn't respond to conservative treatment, consult an orthopedist or rheumatologist for advanced treatment options including injections or surgery."
                }
            ]
        },
        
        # NEUROLOGICAL SYSTEM
        {
            "name": "Tension Headache",
            "variations": [
                {
                    "group": "Adult (18-65)",
                    "prompts": [
                        "I have a dull, aching pain all over my head that feels like a tight band.",
                        "What is a tension headache and how should I treat it?",
                        "My head has been hurting for hours with a pressing sensation.",
                        "I feel like there's pressure around my forehead and temples.",
                        "I have a constant, mild headache that won't go away.",
                        "My head hurts when I'm stressed or tired.",
                        "I have a squeezing sensation around my head."
                    ],
                    "completion": "A dull, band-like pain around the head typically indicates a tension headache. For adults, treatment includes over-the-counter pain relievers (acetaminophen 500-1000mg or ibuprofen 200-400mg), applied heat or cold to the head/neck, gentle neck stretches, and stress management techniques. Ensure adequate sleep (7-9 hours) and stay hydrated. If headaches occur more than 15 days per month, become severe suddenly, or are accompanied by vision changes, seek medical evaluation."
                },
                {
                    "group": "Office Workers",
                    "prompts": [
                        "I get headaches from staring at a computer screen all day.",
                        "How do you prevent computer-related headaches?",
                        "I have eye strain and headaches from work."
                    ],
                    "completion": "Computer-related headaches often result from eye strain, poor posture, or neck tension. Prevention includes following the 20-20-20 rule (every 20 minutes, look at something 20 feet away for 20 seconds), adjusting monitor brightness and position, ensuring proper lighting, and maintaining good posture. Take regular breaks, stay hydrated, and consider computer glasses if eye strain persists. If headaches continue despite ergonomic improvements, consult your healthcare provider to rule out other causes."
                }
            ]
        },
        {
            "name": "Migraine",
            "variations": [
                {
                    "group": "Women (18-50)",
                    "prompts": [
                        "I have a severe one-sided headache with nausea and light sensitivity.",
                        "What are migraine symptoms in women?",
                        "I get terrible headaches around my menstrual cycle.",
                        "How do you treat migraines?",
                        "I have throbbing head pain that makes me nauseous.",
                        "I see flashing lights before my headaches start.",
                        "Light and sound make my headaches much worse."
                    ],
                    "completion": "Severe, one-sided throbbing headache with nausea and light sensitivity strongly suggests migraine. Women often experience hormonal migraines related to menstrual cycles. Acute treatment includes triptans (sumatriptan), NSAIDs, or prescribed migraine medications taken early in the attack. Rest in a dark, quiet room and apply cold compress to the head. For frequent migraines (>4 per month), preventive medications may be needed. Track triggers like stress, certain foods, sleep patterns, and hormonal changes to identify patterns."
                }
            ]
        },
        
        # ENDOCRINE SYSTEM
        {
            "name": "Type 2 Diabetes",
            "variations": [
                {
                    "group": "Adult (35-65)",
                    "prompts": [
                        "I'm always thirsty and urinating frequently. Could this be diabetes?",
                        "What are early signs of type 2 diabetes?",
                        "I feel tired all the time and have been losing weight without trying.",
                        "How do you know if you have diabetes?",
                        "I have excessive thirst and my vision seems blurry lately.",
                        "I'm hungry all the time but still losing weight.",
                        "My cuts heal slowly and I get infections easily."
                    ],
                    "completion": "Excessive thirst, frequent urination, unexplained fatigue, and unintentional weight loss are classic early signs of type 2 diabetes. Blurred vision can also occur due to high blood sugar levels. These symptoms warrant immediate medical evaluation including blood glucose testing. Early detection and management through lifestyle modifications (diet, exercise) and potentially medication can prevent serious complications. Schedule an appointment with your primary care physician for proper testing and diagnosis."
                },
                {
                    "group": "High-Risk Adults (Overweight, Family History)",
                    "prompts": [
                        "I have a family history of diabetes and am overweight. What symptoms should I watch for?",
                        "How can I prevent diabetes if I'm at high risk?",
                        "What are pre-diabetes symptoms?"
                    ],
                    "completion": "With family history and elevated BMI, you're at increased risk for type 2 diabetes. Watch for symptoms like increased thirst, frequent urination, fatigue, slow-healing cuts, or frequent infections. Prevention strategies include maintaining healthy weight through balanced diet, regular physical activity (150 minutes/week), limiting processed foods and sugary drinks. Regular screening with fasting glucose or A1C tests is recommended annually. Early intervention with lifestyle changes can prevent or delay onset of diabetes."
                }
            ]
        },
        {
            "name": "Hypothyroidism",
            "variations": [
                {
                    "group": "Women (30-60)",
                    "prompts": [
                        "I'm always tired, gaining weight, and feel cold all the time.",
                        "What are signs of an underactive thyroid?",
                        "I have fatigue, hair loss, and my periods are irregular.",
                        "How do you know if you have thyroid problems?",
                        "I feel sluggish and my skin is very dry lately.",
                        "I'm constipated and my hair is thinning.",
                        "I feel depressed and can't lose weight despite dieting."
                    ],
                    "completion": "Persistent fatigue, unexplained weight gain, cold intolerance, hair loss, and irregular periods in women may suggest hypothyroidism (underactive thyroid). Other symptoms include dry skin, constipation, and depression. This condition requires blood testing (TSH, T4) for diagnosis. If confirmed, treatment with synthetic thyroid hormone (levothyroxine) is typically very effective. Schedule an appointment with your primary care physician for thyroid function testing if you experience multiple symptoms. Regular monitoring and medication adjustment may be needed."
                }
            ]
        },
        
        # MENTAL HEALTH CONDITIONS
        {
            "name": "Depression",
            "variations": [
                {
                    "group": "Adult (18-65)",
                    "prompts": [
                        "I feel sad most of the time and have lost interest in things I used to enjoy.",
                        "What are signs of depression?",
                        "I have no energy and feel hopeless about the future.",
                        "How do you know if you're depressed?",
                        "I can't concentrate and feel worthless lately.",
                        "I sleep too much but still feel tired all the time.",
                        "I don't enjoy anything anymore and feel empty inside."
                    ],
                    "completion": "Persistent sadness, loss of interest in activities, fatigue, feelings of hopelessness, and difficulty concentrating for more than two weeks may indicate depression. Initial steps include maintaining routine, regular exercise, adequate sleep, connecting with supportive people, and avoiding alcohol/drugs. However, depression is a medical condition that often requires professional treatment. Contact your primary care physician or a mental health professional for proper evaluation. Therapy, medication, or combination treatment can be very effective."
                },
                {
                    "group": "Postpartum Women",
                    "prompts": [
                        "I had a baby 3 months ago and feel constantly sad and overwhelmed.",
                        "What is postpartum depression?",
                        "I don't feel bonded with my baby and cry frequently.",
                        "I feel guilty and anxious about being a mother."
                    ],
                    "completion": "Persistent sadness, overwhelming feelings, and difficulty bonding with your baby after childbirth may indicate postpartum depression, which affects up to 15% of new mothers. This is different from 'baby blues' and requires professional support. Contact your obstetrician, primary care provider, or a mental health professional immediately. Treatment may include therapy, medication (safe during breastfeeding), and support groups. Postpartum depression is treatable, and seeking help is crucial for both mother and baby's wellbeing."
                }
            ]
        },
        {
            "name": "Anxiety Disorder",
            "variations": [
                {
                    "group": "Adult (18-65)",
                    "prompts": [
                        "I feel constantly worried and have trouble sleeping.",
                        "What are symptoms of anxiety disorder?",
                        "I have racing thoughts and feel on edge all the time.",
                        "How do you manage anxiety without medication?",
                        "I get panic attacks and my heart races frequently.",
                        "I worry about everything and can't relax.",
                        "I avoid social situations because they make me anxious."
                    ],
                    "completion": "Persistent worry, racing thoughts, sleep difficulties, and physical symptoms like rapid heartbeat suggest anxiety disorder. Initial management includes regular exercise, deep breathing techniques, mindfulness meditation, limiting caffeine, and maintaining consistent sleep schedule. Cognitive-behavioral therapy (CBT) is highly effective for anxiety. If symptoms significantly impact daily functioning, work, or relationships, consult a mental health professional. Severe anxiety or panic attacks may require medication in combination with therapy."
                },
                {
                    "group": "Teenagers (13-18)",
                    "prompts": [
                        "I'm a teenager and feel anxious about everything, especially school.",
                        "How can teens manage anxiety?",
                        "I worry constantly about tests and social situations."
                    ],
                    "completion": "Anxiety is common during teenage years due to academic pressure, social changes, and hormonal fluctuations. Helpful strategies include regular exercise, adequate sleep (8-10 hours), limiting social media, talking to trusted adults, and practicing relaxation techniques. School counselors can provide support and coping strategies. If anxiety interferes with school performance, relationships, or daily activities, consider counseling with a therapist who specializes in adolescent mental health."
                }
            ]
        },
        
        # DERMATOLOGICAL CONDITIONS
        {
            "name": "Eczema (Atopic Dermatitis)",
            "variations": [
                {
                    "group": "Children (2-12 years)",
                    "prompts": [
                        "My child has red, itchy patches on their arms and legs.",
                        "What does eczema look like in kids?",
                        "My toddler keeps scratching their skin until it bleeds.",
                        "How do you treat childhood eczema?",
                        "My child's skin is dry, red, and constantly itchy.",
                        "The itching keeps my child awake at night."
                    ],
                    "completion": "Red, itchy, dry patches on arms and legs in children often indicate eczema (atopic dermatitis). Treatment includes gentle, fragrance-free moisturizers applied multiple times daily, especially after bathing with lukewarm water and mild soap. Use topical corticosteroids as prescribed for flare-ups. Keep fingernails short to prevent scratching damage. Identify and avoid triggers like certain fabrics, soaps, or foods. If severe itching disrupts sleep or if infection signs appear (pus, increased redness, fever), consult your pediatrician."
                },
                {
                    "group": "Adult (18-65)",
                    "prompts": [
                        "I have persistent itchy, dry skin patches as an adult.",
                        "Can adults develop eczema later in life?",
                        "My hands are red, cracked, and constantly itchy."
                    ],
                    "completion": "Adult-onset eczema can occur, often triggered by stress, environmental factors, or occupational exposures. Management includes regular moisturizing with thick, fragrance-free creams, identifying and avoiding triggers, using gentle detergents and soaps, and managing stress. Topical corticosteroids may be needed for flare-ups. If hand eczema interferes with work or daily activities, or if patches become infected, consult a dermatologist for specialized treatment and allergy testing."
                }
            ]
        },
        {
            "name": "Acne",
            "variations": [
                {
                    "group": "Teenagers (13-19)",
                    "prompts": [
                        "I have pimples and blackheads all over my face.",
                        "What causes teenage acne?",
                        "How do you treat acne breakouts?",
                        "I have oily skin and constant breakouts.",
                        "My acne is affecting my self-confidence."
                    ],
                    "completion": "Facial pimples, blackheads, and oily skin are common during adolescence due to hormonal changes. Basic treatment includes gentle cleansing twice daily with mild soap, using non-comedogenic moisturizers and makeup, and over-the-counter treatments containing benzoyl peroxide or salicylic acid. Avoid over-washing or harsh scrubbing, which can worsen acne. If acne is severe, causes scarring, or significantly affects self-esteem, consult a dermatologist for prescription treatments like topical or oral antibiotics."
                },
                {
                    "group": "Adult Women (20-40)",
                    "prompts": [
                        "I'm an adult woman with hormonal acne around my jawline.",
                        "What causes adult acne in women?",
                        "I get breakouts before my period every month."
                    ],
                    "completion": "Adult women often experience hormonal acne, typically around the jawline and chin, that flares before menstrual periods. This is caused by fluctuating estrogen and progesterone levels. Treatment may include topical retinoids, hormonal therapies like birth control pills or spironolactone, and consistent skincare routine. Anti-inflammatory ingredients like niacinamide can help. If acne significantly impacts quality of life or doesn't respond to over-the-counter treatments, consult a dermatologist for hormonal evaluation and prescription options."
                }
            ]
        },
        
        # INFECTIOUS DISEASES
        {
            "name": "Urinary Tract Infection (UTI)",
            "variations": [
                {
                    "group": "Women (18-65)",
                    "prompts": [
                        "I have burning when I urinate and need to go frequently.",
                        "What are the symptoms of a bladder infection?",
                        "I feel like I need to pee all the time and it hurts.",
                        "How do you treat a UTI in women?",
                        "I have pelvic pain and burning during urination.",
                        "I have urgency and only small amounts of urine come out.",
                        "My urine smells strong and looks cloudy."
                    ],
                    "completion": "Burning during urination with increased frequency and urgency in women often indicates a urinary tract infection (UTI). Immediate care includes drinking plenty of water (at least 8 glasses daily), urinating frequently, and taking over-the-counter pain relievers. However, UTIs typically require antibiotic treatment, so contact your healthcare provider for proper diagnosis and prescription. Seek immediate care if you develop fever, back pain, nausea, or blood in urine, as these may indicate kidney involvement."
                },
                {
                    "group": "Pregnant Women",
                    "prompts": [
                        "I'm pregnant and have UTI symptoms. Is this dangerous?",
                        "Can a bladder infection harm my baby?",
                        "I'm expecting and have burning when I urinate."
                    ],
                    "completion": "UTIs during pregnancy require prompt medical attention as untreated infections can lead to serious complications including preterm labor and kidney infections. Pregnant women with burning urination, frequency, or urgency should contact their obstetrician immediately. Treatment with pregnancy-safe antibiotics is essential. Never delay seeking care for UTI symptoms during pregnancy, and complete the full course of any prescribed antibiotics even if symptoms improve quickly."
                }
            ]
        },
        
        # WOMEN'S HEALTH
        {
            "name": "Menstrual Disorders",
            "variations": [
                {
                    "group": "Women (13-50)",
                    "prompts": [
                        "My periods are very heavy and last longer than a week.",
                        "What are abnormal menstrual symptoms?",
                        "I have severe cramping that interferes with daily activities.",
                        "My periods are irregular and unpredictable.",
                        "I have painful periods with heavy bleeding.",
                        "I miss periods for months at a time.",
                        "I bleed between periods and have pelvic pain."
                    ],
                    "completion": "Heavy periods lasting over 7 days, severe cramping affecting daily activities, or irregular cycles may indicate menstrual disorders like PCOS, endometriosis, or fibroids. Track your cycles, flow, and symptoms in a menstrual diary. Initial management may include hormonal birth control, anti-inflammatory medications for cramping, and lifestyle modifications. Consult a gynecologist if periods significantly impact your life, you have bleeding between periods, or miss multiple cycles. Early evaluation can prevent complications and improve quality of life."
                },
                {
                    "group": "Teenagers (13-19)",
                    "prompts": [
                        "I'm a teenager and my periods are very painful.",
                        "Is it normal for teen periods to be irregular?",
                        "I miss school because of period pain."
                    ],
                    "completion": "While some irregularity is normal in the first 1-2 years after menarche, severe pain interfering with school or activities isn't normal. Treatment for painful periods includes heat therapy, over-the-counter pain relievers (ibuprofen works best for menstrual cramps), gentle exercise, and stress management. If pain is severe, periods are extremely heavy, or significantly impact daily life, consult a gynecologist or pediatrician. Early intervention can prevent complications and improve adolescent quality of life."
                }
            ]
        },
        {
            "name": "Menopause",
            "variations": [
                {
                    "group": "Women (45-60)",
                    "prompts": [
                        "I'm having hot flashes and my periods are irregular.",
                        "What are menopause symptoms?",
                        "I wake up drenched in sweat and feel moody all the time.",
                        "How do you manage menopause naturally?",
                        "I'm 50 and having sleep problems with night sweats.",
                        "I have vaginal dryness and decreased libido.",
                        "My memory seems foggy and I feel emotional."
                    ],
                    "completion": "Hot flashes, night sweats, irregular periods, and mood changes in women around age 50 suggest perimenopause or menopause. Natural management includes regular exercise, maintaining healthy weight, limiting caffeine and alcohol, dressing in layers, using fans, and stress reduction techniques. Dietary approaches like soy products may help some women. For severe symptoms affecting quality of life, hormone replacement therapy or other medications may be appropriate. Consult your gynecologist to discuss symptom management options and long-term health considerations."
                }
            ]
        },
        
        # MEN'S HEALTH
        {
            "name": "Erectile Dysfunction",
            "variations": [
                {
                    "group": "Men (40-70)",
                    "prompts": [
                        "I'm having difficulty maintaining an erection.",
                        "What causes erectile dysfunction?",
                        "I have problems with sexual performance and it's affecting my relationship.",
                        "How do you treat ED?",
                        "I'm a middle-aged man with erection problems.",
                        "I can get an erection but can't maintain it.",
                        "My sexual performance has declined gradually over months."
                    ],
                    "completion": "Difficulty achieving or maintaining erections sufficient for sexual activity suggests erectile dysfunction (ED), affecting about 40% of men over 40. Causes include cardiovascular disease, diabetes, stress, relationship issues, or medication side effects. Initial steps include lifestyle modifications: regular exercise, healthy diet, weight management, limiting alcohol, and quitting smoking. Address underlying health conditions and review medications with your doctor. If lifestyle changes don't help, consult a urologist for evaluation and treatment options including medications, devices, or other therapies."
                }
            ]
        },
        {
            "name": "Enlarged Prostate (BPH)",
            "variations": [
                {
                    "group": "Men (50+)",
                    "prompts": [
                        "I have trouble starting urination and my stream is weak.",
                        "What are prostate enlargement symptoms?",
                        "I wake up multiple times at night to urinate.",
                        "I feel like I can't empty my bladder completely.",
                        "I have urgent need to urinate but only small amounts come out."
                    ],
                    "completion": "Difficulty starting urination, weak stream, frequent nighttime urination, and feeling of incomplete bladder emptying in men over 50 suggest benign prostatic hyperplasia (enlarged prostate). Initial management includes limiting fluids before bedtime, avoiding caffeine and alcohol, and double voiding. If symptoms significantly impact quality of life or you develop urinary retention, consult a urologist. Treatment options include medications to relax prostate muscles or shrink the gland, and surgical procedures for severe cases."
                }
            ]
        },
        
        # ALLERGIC CONDITIONS
        {
            "name": "Seasonal Allergies",
            "variations": [
                {
                    "group": "Adult (18-65)",
                    "prompts": [
                        "I have itchy, watery eyes and keep sneezing, especially outdoors.",
                        "What are the symptoms of seasonal allergies?",
                        "How do I know if I have hay fever?",
                        "I'm sneezing a lot during spring. Is this allergies?",
                        "My eyes are red and itchy, and my nose won't stop running.",
                        "I feel congested every morning during allergy season.",
                        "I have post-nasal drip and chronic throat clearing."
                    ],
                    "completion": "Itchy, watery eyes with sneezing, especially when outdoors during certain seasons, suggests seasonal allergies (hay fever). Treatment includes antihistamines like loratadine (Claritin) or cetirizine (Zyrtec), nasal corticosteroid sprays, and avoiding known allergens when possible. Keep windows closed during high pollen days, shower after being outdoors, and use air purifiers indoors. If symptoms significantly impact daily life or don't respond to over-the-counter treatments, consult an allergist for testing and prescription medications."
                }
            ]
        },
        
        # SLEEP DISORDERS
        {
            "name": "Insomnia",
            "variations": [
                {
                    "group": "Adult (25-65)",
                    "prompts": [
                        "I can't fall asleep and toss and turn for hours every night.",
                        "What are good sleep hygiene practices?",
                        "I wake up multiple times during the night and can't get back to sleep.",
                        "How do you treat insomnia naturally?",
                        "I feel tired during the day because I can't sleep well at night.",
                        "I lie awake worrying and my mind won't shut off.",
                        "I wake up at 3 AM every night and can't fall back asleep."
                    ],
                    "completion": "Chronic difficulty falling or staying asleep suggests insomnia. Improve sleep hygiene by maintaining consistent sleep/wake times, creating a cool, dark sleeping environment, avoiding screens 1 hour before bed, limiting caffeine after 2 PM, and establishing a relaxing bedtime routine. Regular exercise helps but not within 3 hours of bedtime. If sleep problems persist for more than 3 weeks or significantly impact daily functioning, consult a healthcare provider for evaluation of underlying causes and potential treatment options."
                }
            ]
        },
        {
            "name": "Sleep Apnea",
            "variations": [
                {
                    "group": "Overweight Men (35-65)",
                    "prompts": [
                        "I snore loudly and my partner says I stop breathing during sleep.",
                        "What are sleep apnea symptoms?",
                        "I wake up gasping for air and feel tired despite sleeping 8 hours.",
                        "How do you treat sleep apnea?",
                        "I have morning headaches and feel exhausted during the day."
                    ],
                    "completion": "Loud snoring with breathing interruptions, gasping during sleep, morning headaches, and daytime fatigue despite adequate sleep time suggest sleep apnea. This serious condition increases cardiovascular risks and requires medical evaluation with a sleep study. Treatment may include CPAP machine, weight loss, sleeping on your side, avoiding alcohol before bed, and treating nasal congestion. Untreated sleep apnea increases risk of high blood pressure, heart disease, and stroke. Consult a sleep specialist for proper diagnosis and treatment planning."
                }
            ]
        },
        
        # EMERGENCY SYMPTOM COMBINATIONS
        {
            "name": "Chest Pain (Emergency)",
            "variations": [
                {
                    "group": "Adults (All)",
                    "prompts": [
                        "I have severe chest pain that feels like pressure and radiates to my arm.",
                        "I have crushing chest pain with sweating and nausea.",
                        "My chest hurts and I'm having trouble breathing.",
                        "I have chest pain that came on suddenly and is very severe."
                    ],
                    "completion": "Severe chest pain, especially with pressure sensation, arm radiation, sweating, nausea, or breathing difficulties, could indicate a heart attack or other serious cardiac condition. This is a medical emergency. Call 911 immediately - do not drive yourself to the hospital. While waiting for emergency services, chew an aspirin if not allergic, sit upright, and try to stay calm. Time is critical in treating heart attacks, so seek immediate emergency medical care."
                }
            ]
        },
        {
            "name": "Severe Headache (Emergency)",
            "variations": [
                {
                    "group": "Adults (All)",
                    "prompts": [
                        "I have the worst headache of my life that came on suddenly.",
                        "I have severe headache with neck stiffness and high fever.",
                        "My head hurts severely and I'm seeing double.",
                        "I have a thunderclap headache that peaked within seconds."
                    ],
                    "completion": "Sudden, severe headache described as 'the worst of your life,' especially with neck stiffness, fever, vision changes, or neurological symptoms, could indicate serious conditions like meningitis, brain hemorrhage, or stroke. This is a medical emergency requiring immediate evaluation. Call 911 or go to the emergency room immediately. Do not wait or try to treat with over-the-counter medications. These symptoms require urgent medical assessment and potentially life-saving treatment."
                }
            ]
        },
        
        # SYMPTOM COMBINATIONS
        {
            "name": "Flu-like Syndrome",
            "variations": [
                {
                    "group": "Adult (18-65)",
                    "prompts": [
                        "I have fever, body aches, headache, and feel terrible all over.",
                        "What does it mean to have flu-like symptoms?",
                        "I have chills, muscle pain, and fatigue with low-grade fever.",
                        "I feel like I was hit by a truck with aches and fever.",
                        "I have general malaise with body aches and mild fever."
                    ],
                    "completion": "Fever, body aches, headache, and general malaise describe flu-like symptoms that can occur with various viral infections, early bacterial infections, or other conditions. Focus on rest, hydration, and symptom management with over-the-counter medications. Monitor temperature and symptoms closely. Seek medical attention if fever exceeds 103°F, symptoms worsen rapidly, you develop breathing difficulties, or if you're in a high-risk group (over 65, pregnant, or have chronic conditions). Most viral illnesses resolve within 7-10 days."
                }
            ]
        },
        {
            "name": "Dehydration",
            "variations": [
                {
                    "group": "Adults (All)",
                    "prompts": [
                        "I feel dizzy, tired, and my mouth is very dry.",
                        "What are signs of dehydration?",
                        "I have a headache and dark yellow urine.",
                        "I'm not urinating much and feel weak.",
                        "I have been vomiting and now feel lightheaded."
                    ],
                    "completion": "Dizziness, dry mouth, headache, dark urine, and decreased urination suggest dehydration. Mild dehydration can be treated by gradually drinking clear fluids - water, clear broths, or oral rehydration solutions. Avoid large amounts at once if nauseous. Rest in a cool environment and monitor urine color (should become lighter). Seek medical attention if you have persistent vomiting, signs of severe dehydration (confusion, rapid heartbeat, no urination for 8+ hours), or if dehydration results from serious illness."
                },
                {
                    "group": "Elderly (65+)",
                    "prompts": [
                        "I'm elderly and feel confused with decreased urination.",
                        "How does dehydration affect seniors?",
                        "I'm 80 and haven't been drinking much water lately."
                    ],
                    "completion": "Elderly adults are at higher risk for dehydration due to decreased thirst sensation, kidney function changes, and medications. Dehydration in seniors can cause confusion, falls, constipation, and urinary tract infections. Signs include dry mouth, decreased skin elasticity, dark urine, and altered mental status. Encourage regular fluid intake throughout the day, even without feeling thirsty. If an elderly person shows confusion, weakness, or hasn't urinated in 8+ hours, seek medical attention immediately as dehydration can be life-threatening in this population."
                }
            ]
        },
        
        # ADDITIONAL COMMON CONDITIONS
        {
            "name": "Strep Throat",
            "variations": [
                {
                    "group": "Children (5-15 years)",
                    "prompts": [
                        "My child has a severe sore throat and white patches on their tonsils.",
                        "What are strep throat symptoms in kids?",
                        "My child has fever and says it hurts to swallow.",
                        "How do you treat strep throat?",
                        "My kid's throat is very red with white spots and they have a fever."
                    ],
                    "completion": "Severe sore throat with white patches on tonsils, fever, and difficulty swallowing in children suggests strep throat, a bacterial infection requiring antibiotic treatment. Have the child tested with a rapid strep test or throat culture. While waiting for medical care, provide soft foods, warm salt water gargles (if age-appropriate), pain relievers, and plenty of fluids. Children can return to school 24 hours after starting antibiotics and being fever-free. Complete the full course of antibiotics to prevent complications like rheumatic fever."
                }
            ]
        },
        {
            "name": "Constipation",
            "variations": [
                {
                    "group": "Adult (18-65)",
                    "prompts": [
                        "I haven't had a bowel movement in 3 days and feel bloated.",
                        "What causes constipation and how do you treat it?",
                        "I have hard, dry stools that are difficult to pass.",
                        "I feel full and uncomfortable from constipation.",
                        "I strain when trying to have a bowel movement."
                    ],
                    "completion": "Infrequent, hard, difficult-to-pass stools with bloating suggest constipation. Treatment includes increasing fiber intake gradually (25-35g daily), drinking more water (8-10 glasses daily), regular physical activity, and establishing regular toilet habits. Over-the-counter stool softeners or gentle laxatives may help short-term. Avoid prolonged use of stimulant laxatives. If constipation persists despite lifestyle changes, is accompanied by severe pain, or you notice blood in stool, consult your healthcare provider to rule out underlying conditions."
                },
                {
                    "group": "Elderly (65+)",
                    "prompts": [
                        "I'm elderly and have chronic constipation problems.",
                        "How does aging affect bowel movements?",
                        "I'm a senior and often go days without a bowel movement."
                    ],
                    "completion": "Constipation is common in elderly adults due to decreased mobility, medications, reduced fluid intake, and age-related changes in digestive function. Management includes adequate fluid intake, fiber-rich foods (if tolerated), gentle exercise like walking, and establishing regular bathroom routines. Many medications used by seniors can cause constipation. Work with your healthcare provider to review medications and develop a bowel management plan. Sudden changes in bowel habits or severe constipation may indicate serious conditions requiring evaluation."
                }
            ]
        },
        {
            "name": "Diarrhea",
            "variations": [
                {
                    "group": "Adult (18-65)",
                    "prompts": [
                        "I have frequent loose, watery stools and stomach cramping.",
                        "What causes sudden diarrhea?",
                        "I have urgent bowel movements and can't control timing.",
                        "How do you treat acute diarrhea?",
                        "I have diarrhea with nausea and feel dehydrated."
                    ],
                    "completion": "Frequent loose, watery stools with cramping suggest acute diarrhea, commonly caused by viral infections, food poisoning, or dietary factors. Focus on preventing dehydration with clear fluids, oral rehydration solutions, and electrolyte replacement. Follow the BRAT diet when tolerated. Avoid dairy, caffeine, alcohol, and fatty foods. Most acute diarrhea resolves within 3-7 days. Seek medical care if you have blood in stool, high fever, signs of dehydration, severe abdominal pain, or if symptoms persist beyond a week."
                }
            ]
        },
        
        # PAIN CONDITIONS
        {
            "name": "Fibromyalgia",
            "variations": [
                {
                    "group": "Women (30-60)",
                    "prompts": [
                        "I have widespread pain all over my body and feel exhausted.",
                        "What are fibromyalgia symptoms?",
                        "I ache everywhere and my sleep is terrible.",
                        "How do you manage fibromyalgia pain?",
                        "I have tender points all over and feel like I have the flu constantly.",
                        "I wake up stiff and sore every morning with fatigue.",
                        "I have muscle pain that migrates around my body."
                    ],
                    "completion": "Widespread body pain, fatigue, and sleep disturbances affecting multiple tender points suggest fibromyalgia, more common in women. Management involves a multidisciplinary approach: regular low-impact exercise (swimming, walking, tai chi), stress management techniques, consistent sleep schedule, and pain management strategies. Medications may include pregabalin, duloxetine, or low-dose antidepressants. Cognitive-behavioral therapy can help cope with chronic pain. Consult a rheumatologist for proper diagnosis and comprehensive treatment plan."
                }
            ]
        },
        
        # SKIN CONDITIONS
        {
            "name": "Psoriasis",
            "variations": [
                {
                    "group": "Adults (20-60)",
                    "prompts": [
                        "I have thick, scaly, red patches on my elbows and knees.",
                        "What are psoriasis symptoms?",
                        "My skin has silvery scales and is very itchy.",
                        "How do you treat psoriasis?",
                        "I have raised, red patches with flaky skin that won't go away.",
                        "My scalp is scaly and itchy with thick patches.",
                        "I have nail changes with pitting and ridges."
                    ],
                    "completion": "Thick, red, scaly patches with silvery scales, commonly on elbows, knees, and scalp, suggest psoriasis, an autoimmune skin condition. Treatment varies by severity: mild cases may respond to topical corticosteroids, moisturizers, and coal tar preparations. Moderate to severe cases may require systemic medications or biologics. Stress management, avoiding skin trauma, and moderate sun exposure can help. Psoriasis is associated with increased cardiovascular risk, so maintain heart-healthy lifestyle. Consult a dermatologist for proper diagnosis and treatment planning."
                }
            ]
        },
        
        # NUTRITIONAL/METABOLIC
        {
            "name": "Iron Deficiency Anemia",
            "variations": [
                {
                    "group": "Women of Childbearing Age",
                    "prompts": [
                        "I feel exhausted all the time and my periods are very heavy.",
                        "What causes iron deficiency in women?",
                        "I'm pale, tired, and my nails are brittle.",
                        "How do you treat iron deficiency anemia?",
                        "I get short of breath easily and feel weak.",
                        "I crave ice and starch, and feel tired constantly.",
                        "My hair is falling out and I have no energy."
                    ],
                    "completion": "Persistent fatigue, pale skin, brittle nails, and shortness of breath in women of childbearing age often indicate iron deficiency anemia, commonly caused by heavy menstrual periods. Treatment includes iron supplements (take with vitamin C for better absorption, avoid with dairy/coffee), increasing iron-rich foods (lean meats, beans, spinach, fortified cereals), and addressing underlying causes like heavy periods. Blood tests are needed to confirm diagnosis and monitor treatment response. Consult your healthcare provider for proper evaluation and iron studies."
                }
            ]
        },
        {
            "name": "Vitamin D Deficiency",
            "variations": [
                {
                    "group": "Adults (25-65)",
                    "prompts": [
                        "I feel tired all the time and my bones ache.",
                        "What are symptoms of vitamin D deficiency?",
                        "I have muscle weakness and feel depressed.",
                        "How do you treat low vitamin D?",
                        "I don't get much sun and feel exhausted constantly.",
                        "I have bone pain and frequent muscle cramps.",
                        "I live in a northern climate and feel sluggish all winter."
                    ],
                    "completion": "Persistent fatigue, bone aches, muscle weakness, and mood changes, especially with limited sun exposure, may indicate vitamin D deficiency. This is common in northern climates and people who spend most time indoors. Treatment includes vitamin D3 supplements (typically 1000-2000 IU daily), increasing foods rich in vitamin D (fatty fish, fortified milk, egg yolks), and safe sun exposure (10-30 minutes daily depending on skin type). Blood testing is needed to confirm deficiency and monitor treatment response. Consult your healthcare provider for proper testing and dosing recommendations."
                }
            ]
        },
        
        # JOINT/BONE CONDITIONS
        {
            "name": "Rheumatoid Arthritis",
            "variations": [
                {
                    "group": "Women (30-60)",
                    "prompts": [
                        "I have joint pain and stiffness that's worse in the morning and affects both hands.",
                        "What are rheumatoid arthritis symptoms?",
                        "My joints are swollen, warm, and very stiff in the morning.",
                        "I have fatigue and joint pain in multiple joints.",
                        "My hands and feet are swollen and painful symmetrically."
                    ],
                    "completion": "Symmetric joint pain and swelling, particularly in hands and feet, with prolonged morning stiffness (>1 hour) and systemic symptoms like fatigue suggest rheumatoid arthritis, an autoimmune condition. Early diagnosis and treatment are crucial to prevent joint damage. Blood tests (RF, anti-CCP) and imaging help confirm diagnosis. Treatment includes disease-modifying medications, anti-inflammatory drugs, physical therapy, and lifestyle modifications. Consult a rheumatologist promptly for evaluation, as early aggressive treatment leads to better long-term outcomes."
                }
            ]
        },
        
        # EYE CONDITIONS
        {
            "name": "Conjunctivitis (Pink Eye)",
            "variations": [
                {
                    "group": "Children (2-12 years)",
                    "prompts": [
                        "My child's eye is red with thick yellow discharge.",
                        "What are pink eye symptoms in kids?",
                        "My child woke up with their eye stuck shut from discharge.",
                        "How do you treat bacterial pink eye?",
                        "One of my child's eyes is very red and has pus coming out."
                    ],
                    "completion": "Thick yellow or green eye discharge with redness, especially if the eye is 'glued shut' in the morning, suggests bacterial conjunctivitis (pink eye). This is highly contagious and requires antibiotic eye drops or ointment prescribed by a healthcare provider. Keep the child home from school/daycare until treated for 24 hours. Clean discharge gently with warm water, wash hands frequently, and avoid sharing towels or pillowcases. Contact your pediatrician for proper diagnosis and prescription treatment."
                },
                {
                    "group": "Adult (18-65)",
                    "prompts": [
                        "My eye is red, irritated, and has thick discharge.",
                        "How do you know if pink eye is bacterial or viral?",
                        "I have gritty feeling in my eye with yellow discharge."
                    ],
                    "completion": "Red, irritated eyes with thick, colored discharge typically indicate bacterial conjunctivitis, which requires antibiotic treatment. Bacterial conjunctivitis usually affects one eye initially and produces more purulent discharge than viral pink eye. Clean the eye gently with warm water, avoid touching or rubbing the eye, and wash hands frequently to prevent spread. Contact your healthcare provider for antibiotic eye drops. Avoid contact lenses until infection clears and you've completed treatment."
                }
            ]
        },
        
        # HORMONAL CONDITIONS
        {
            "name": "PCOS (Polycystic Ovary Syndrome)",
            "variations": [
                {
                    "group": "Women (15-45)",
                    "prompts": [
                        "I have irregular periods, weight gain, and excess hair growth.",
                        "What are PCOS symptoms?",
                        "I missed several periods and have acne and hair loss.",
                        "How do you treat polycystic ovary syndrome?",
                        "I have difficulty losing weight and irregular cycles."
                    ],
                    "completion": "Irregular periods, weight gain, excess hair growth (hirsutism), acne, and difficulty losing weight suggest PCOS (polycystic ovary syndrome). This hormonal disorder affects up to 10% of women of reproductive age. Management includes lifestyle modifications (healthy diet, regular exercise, weight management), hormonal birth control to regulate periods, and medications for insulin resistance if present. PCOS increases risk of diabetes and cardiovascular disease, so regular monitoring is important. Consult a gynecologist or endocrinologist for proper diagnosis and comprehensive management plan."
                }
            ]
        },
        
        # ADDITIONAL COMPREHENSIVE CONDITIONS
        {
            "name": "Kidney Stones",
            "variations": [
                {
                    "group": "Adult (30-60)",
                    "prompts": [
                        "I have severe pain in my side that comes in waves and blood in my urine.",
                        "What are kidney stone symptoms?",
                        "I have excruciating back pain that radiates to my groin.",
                        "How do you treat kidney stones?",
                        "I have sharp pain that makes me nauseous and can't find a comfortable position.",
                        "I feel like someone is stabbing me in the back and I see blood when I urinate.",
                        "I have pain that started in my back and moved to my lower abdomen."
                    ],
                    "completion": "Severe, wave-like flank pain radiating to the groin with blood in urine strongly suggests kidney stones. This is a medical emergency requiring immediate evaluation. Pain management may include prescription medications, and treatment depends on stone size and location. Drink plenty of water to help flush the stone, strain urine to catch passed stones, and seek immediate medical attention. Large stones may require medical procedures. Once resolved, prevention includes increased water intake (2-3 liters daily) and dietary modifications based on stone composition analysis."
                }
            ]
        },
        {
            "name": "Gallbladder Disease",
            "variations": [
                {
                    "group": "Women (40-60)",
                    "prompts": [
                        "I have severe right upper abdominal pain after eating fatty foods.",
                        "What are gallbladder attack symptoms?",
                        "I have pain under my right rib that radiates to my shoulder blade.",
                        "How do you treat gallbladder problems?",
                        "I feel nauseous and have intense pain after eating fried food.",
                        "I have right-sided pain that gets worse after meals.",
                        "I have indigestion and right shoulder pain after eating."
                    ],
                    "completion": "Severe right upper abdominal pain after fatty meals, radiating to the shoulder blade with nausea, suggests gallbladder disease (gallstones or cholecystitis). This is more common in women over 40. Acute attacks require medical evaluation and may need emergency care if pain is severe, you have fever, or jaundice develops. Treatment may involve dietary modifications (low-fat diet), pain management, and potentially surgical removal of the gallbladder. Seek immediate medical attention for severe abdominal pain, especially if accompanied by fever, vomiting, or yellowing of skin/eyes."
                }
            ]
        },
        {
            "name": "Appendicitis",
            "variations": [
                {
                    "group": "Young Adults (15-35)",
                    "prompts": [
                        "I have severe pain that started around my belly button and moved to my right side.",
                        "What are appendicitis symptoms?",
                        "I have right lower abdominal pain with nausea and fever.",
                        "How serious is appendicitis?",
                        "I have pain that gets worse when I walk or cough, located in my right lower abdomen.",
                        "I can't stand up straight because of severe right-sided pain.",
                        "I have stomach pain that started mild but is getting much worse."
                    ],
                    "completion": "Severe abdominal pain starting around the navel and moving to the right lower abdomen, with nausea, fever, and worsening with movement, strongly suggests acute appendicitis. This is a surgical emergency requiring immediate medical attention. Do not eat, drink, or take pain medications as surgery may be needed. Go to the emergency room immediately or call 911. Appendicitis can progress to rupture within hours, leading to life-threatening complications. Prompt surgical removal (appendectomy) is the standard treatment and is usually performed laparoscopically."
                }
            ]
        },
        {
            "name": "Sciatica",
            "variations": [
                {
                    "group": "Adult (35-65)",
                    "prompts": [
                        "I have shooting pain down my leg from my lower back.",
                        "What is sciatica and how do you treat it?",
                        "I have numbness and tingling that goes from my back to my foot.",
                        "My leg pain is worse when I sit or cough.",
                        "I have burning pain that travels down the back of my leg.",
                        "I can't sit comfortably because of leg pain.",
                        "I have weakness in my leg along with the shooting pain."
                    ],
                    "completion": "Shooting pain radiating from the lower back down the leg, often with numbness or tingling, suggests sciatica caused by sciatic nerve irritation. Initial treatment includes anti-inflammatory medications, ice/heat therapy, gentle stretching, and avoiding prolonged sitting. Most cases improve within 4-6 weeks with conservative treatment. Physical therapy can help with specific exercises. Seek immediate medical attention if you experience loss of bladder/bowel control, severe leg weakness, or progressive numbness, as these may indicate serious nerve compression requiring urgent treatment."
                }
            ]
        },
        {
            "name": "Plantar Fasciitis",
            "variations": [
                {
                    "group": "Adults (30-60)",
                    "prompts": [
                        "I have sharp heel pain when I first get out of bed in the morning.",
                        "What causes heel pain when walking?",
                        "My foot hurts worst in the morning and after sitting for a while.",
                        "How do you treat plantar fasciitis?",
                        "I have stabbing pain in the bottom of my heel.",
                        "My heel pain is worse after exercise or long periods of standing.",
                        "I feel like I'm stepping on a nail in my heel."
                    ],
                    "completion": "Sharp heel pain, especially with first steps in the morning or after periods of rest, typically indicates plantar fasciitis. Treatment includes rest from aggravating activities, ice application for 15-20 minutes after activity, calf and plantar fascia stretching exercises, supportive footwear with good arch support, and over-the-counter anti-inflammatory medications. Avoid walking barefoot on hard surfaces. Most cases improve with conservative treatment over several months. If pain persists despite 6 weeks of treatment or significantly limits mobility, consult a podiatrist or orthopedist."
                }
            ]
        },
        {
            "name": "Carpal Tunnel Syndrome",
            "variations": [
                {
                    "group": "Office Workers (25-55)",
                    "prompts": [
                        "My hands tingle and go numb, especially at night.",
                        "What are carpal tunnel symptoms?",
                        "I have wrist pain from computer work and my fingers feel numb.",
                        "How do you treat carpal tunnel syndrome?",
                        "My thumb, index, and middle fingers are numb and weak.",
                        "I wake up with my hands asleep and have to shake them.",
                        "I drop things because my hands feel weak and numb."
                    ],
                    "completion": "Numbness and tingling in the thumb, index, and middle fingers, especially at night, suggests carpal tunnel syndrome. For office workers, treatment includes ergonomic workplace modifications, wrist splints (especially at night), frequent breaks from repetitive activities, and wrist/hand exercises. Adjust keyboard and mouse position to maintain neutral wrist alignment. Anti-inflammatory medications can help reduce swelling. If symptoms persist despite conservative treatment or you experience muscle weakness, consult an orthopedist or neurologist for nerve conduction studies and advanced treatment options."
                }
            ]
        },
        
        # INFECTIOUS DISEASES
        {
            "name": "Cellulitis",
            "variations": [
                {
                    "group": "Adult (25-75)",
                    "prompts": [
                        "I have a red, warm, swollen area on my leg that's painful to touch.",
                        "What are signs of skin infection?",
                        "My skin is red and hot with red streaking lines.",
                        "How serious is cellulitis?",
                        "I have an area of skin that's become increasingly red and tender.",
                        "I have a cut that's become infected and is spreading.",
                        "I have red streaks going up my arm from a wound."
                    ],
                    "completion": "Red, warm, swollen, tender skin, especially with red streaking, suggests cellulitis, a serious bacterial skin infection. This requires immediate antibiotic treatment to prevent spread to deeper tissues or bloodstream. Seek medical attention promptly - same day if possible. Treatment typically involves oral antibiotics for 7-10 days, elevation of affected area, and pain management. Mark the border of redness to monitor progression. Seek emergency care if you develop fever, red streaking toward the heart, or if the infection spreads rapidly despite treatment."
                }
            ]
        },
        {
            "name": "Shingles (Herpes Zoster)",
            "variations": [
                {
                    "group": "Adults (50+)",
                    "prompts": [
                        "I have a painful rash with blisters on one side of my torso.",
                        "What are shingles symptoms?",
                        "I have burning pain followed by a blistery rash in a strip pattern.",
                        "How do you treat shingles?",
                        "I have severe nerve pain and a rash that wraps around my ribcage.",
                        "I have a painful rash that follows a band around my body.",
                        "I had burning pain for days before this rash appeared."
                    ],
                    "completion": "A painful, blistering rash in a band-like pattern on one side of the body suggests shingles (herpes zoster), caused by reactivation of the chickenpox virus. This is most common in adults over 50 or those with weakened immunity. Antiviral medications (acyclovir, valacyclovir) are most effective when started within 72 hours of rash onset. Pain management includes prescription medications, cool compresses, and keeping the rash clean and covered. Seek prompt medical attention for early antiviral treatment to reduce severity and prevent complications like postherpetic neuralgia."
                }
            ]
        },
        
        # REPRODUCTIVE HEALTH
        {
            "name": "Yeast Infection",
            "variations": [
                {
                    "group": "Women (18-65)",
                    "prompts": [
                        "I have thick white vaginal discharge with severe itching.",
                        "What are yeast infection symptoms?",
                        "I have vaginal burning and cottage cheese-like discharge.",
                        "How do you treat a vaginal yeast infection?",
                        "I have vulvar itching and pain during urination.",
                        "I have no odor but thick white discharge and intense itching."
                    ],
                    "completion": "Thick, white, cottage cheese-like vaginal discharge with intense itching and burning suggests a vaginal yeast infection (candidiasis). Over-the-counter antifungal treatments (miconazole, clotrimazole) are usually effective for uncomplicated infections. Avoid douching, wear cotton underwear, and keep the area dry. If this is your first infection, symptoms don't improve with treatment, or you have recurrent infections (>4 per year), consult your healthcare provider for proper diagnosis and evaluation of underlying causes."
                }
            ]
        },
        
        # AUTOIMMUNE CONDITIONS
        {
            "name": "Lupus (SLE)",
            "variations": [
                {
                    "group": "Women (15-45)",
                    "prompts": [
                        "I have a butterfly rash across my cheeks and joint pain.",
                        "What are lupus symptoms?",
                        "I have fatigue, joint pain, and skin rashes.",
                        "I'm sensitive to sunlight and have mouth ulcers.",
                        "I have muscle pain, fatigue, and my fingers turn white in the cold."
                    ],
                    "completion": "A butterfly-shaped facial rash with joint pain, fatigue, and sun sensitivity may suggest systemic lupus erythematosus (SLE), an autoimmune disease most common in women of childbearing age. Other symptoms include mouth ulcers, hair loss, and Raynaud's phenomenon (fingers turning white/blue in cold). Lupus requires specialized medical evaluation with blood tests (ANA, anti-dsDNA) for diagnosis. Treatment involves immunosuppressive medications, sun protection, and regular monitoring. Consult a rheumatologist for proper evaluation if you have multiple suggestive symptoms."
                }
            ]
        },
        
        # SUBSTANCE-RELATED CONDITIONS
        {
            "name": "Alcohol Withdrawal",
            "variations": [
                {
                    "group": "Adults (25-65)",
                    "prompts": [
                        "I stopped drinking and now have shaking hands and sweating.",
                        "What are alcohol withdrawal symptoms?",
                        "I quit drinking and feel anxious with tremors.",
                        "I have nausea and headaches since stopping alcohol.",
                        "I stopped drinking and can't sleep with racing heart."
                    ],
                    "completion": "Tremors, sweating, anxiety, nausea, and sleep disturbances after stopping alcohol suggest withdrawal symptoms. Mild withdrawal can be managed with hydration, rest, and gradual reduction rather than sudden cessation. However, alcohol withdrawal can be dangerous and potentially life-threatening. If you experience severe symptoms, confusion, seizures, or hallucinations, seek immediate medical attention. Medical supervision during detoxification is often necessary for safety. Contact your healthcare provider or an addiction specialist for proper withdrawal management and ongoing support."
                }
            ]
        },
        
        # OCCUPATIONAL/LIFESTYLE CONDITIONS
        {
            "name": "Computer Vision Syndrome",
            "variations": [
                {
                    "group": "Office Workers (25-55)",
                    "prompts": [
                        "My eyes are tired and dry from computer work.",
                        "I have eye strain and headaches from screens.",
                        "My vision is blurry after working on computer all day.",
                        "How do you prevent computer eye strain?",
                        "I have dry eyes and neck pain from desk work."
                    ],
                    "completion": "Eye fatigue, dryness, blurred vision, and headaches from prolonged computer use indicate computer vision syndrome. Prevention includes the 20-20-20 rule (every 20 minutes, look at something 20 feet away for 20 seconds), adjusting screen brightness and contrast, positioning monitor 20-26 inches away at slightly below eye level, and blinking frequently. Use artificial tears for dry eyes and ensure proper lighting to reduce glare. If symptoms persist, consider computer glasses or consult an eye care professional."
                }
            ]
        },
        {
            "name": "Heat Exhaustion",
            "variations": [
                {
                    "group": "Adults (All)",
                    "prompts": [
                        "I've been in hot weather and feel dizzy, nauseous, and weak.",
                        "What are heat exhaustion symptoms?",
                        "I'm sweating heavily and have a headache from the heat.",
                        "I feel faint and sick after being outside in hot weather.",
                        "I'm overheated and feel like I might pass out."
                    ],
                    "completion": "Dizziness, nausea, weakness, heavy sweating, and headache after heat exposure suggest heat exhaustion. Move to a cool environment immediately, remove excess clothing, apply cool water to skin, and drink cool fluids if not nauseous. Rest in air conditioning or shade and monitor symptoms. Most cases improve with cooling and hydration. Seek immediate medical attention if symptoms worsen, you develop confusion, stop sweating despite heat, or have signs of heat stroke (altered mental status, high body temperature). Prevention includes staying hydrated and avoiding prolonged heat exposure."
                }
            ]
        },
        {
            "name": "Vertigo",
            "variations": [
                {
                    "group": "Adults (30-70)",
                    "prompts": [
                        "I feel like the room is spinning when I move my head.",
                        "What causes vertigo and dizziness?",
                        "I have severe dizziness with nausea when I change positions.",
                        "I feel off-balance and the world seems to be moving.",
                        "I get dizzy when I roll over in bed or look up."
                    ],
                    "completion": "Room-spinning sensation triggered by head movements suggests vertigo, often caused by inner ear problems like BPPV (benign positional vertigo). Initial management includes moving slowly, avoiding sudden head movements, staying hydrated, and sitting or lying down during episodes. Simple repositioning exercises (Epley maneuver) may help BPPV. If vertigo is severe, persistent, or accompanied by hearing loss, neurological symptoms, or severe headache, seek medical evaluation to determine the underlying cause and appropriate treatment."
                }
            ]
        },
        {
            "name": "Rosacea",
            "variations": [
                {
                    "group": "Adults (30-60)",
                    "prompts": [
                        "My face is red and flushed, especially my nose and cheeks.",
                        "What are symptoms of rosacea?",
                        "I have persistent redness and small bumps on my face.",
                        "How do you treat rosacea?",
                        "My face burns and stings, and I see visible blood vessels.",
                        "I have facial redness that gets worse with sun or alcohol.",
                        "I have bumps on my face that look like acne but I'm middle-aged."
                    ],
                    "completion": "Persistent facial redness, especially on the nose and cheeks, with burning/stinging sensations and visible blood vessels suggests rosacea. This chronic skin condition requires gentle skincare with fragrance-free products, daily broad-spectrum sunscreen (SPF 30+), and identifying/avoiding triggers like spicy foods, alcohol, extreme temperatures, or stress. Use lukewarm water for cleansing and avoid harsh scrubs. If symptoms worsen or affect self-esteem, consult a dermatologist for prescription treatments like topical antibiotics or oral medications."
                }
            ]
        },
        {
            "name": "Gout",
            "variations": [
                {
                    "group": "Men (40-70)",
                    "prompts": [
                        "I have sudden, severe pain in my big toe that's red and swollen.",
                        "What are gout symptoms?",
                        "My toe joint is extremely painful and I can't touch it.",
                        "I have intense joint pain that came on overnight.",
                        "My foot is so painful I can't put weight on it."
                    ],
                    "completion": "Sudden, severe pain in the big toe (or other joints) with redness, swelling, and extreme tenderness suggests gout, caused by uric acid crystal deposits. Acute attacks require immediate treatment with anti-inflammatory medications, ice application, rest, and elevation. Avoid aspirin during attacks. Long-term management includes dietary modifications (limit purine-rich foods like red meat, organ meats, certain seafood), weight management, adequate hydration, and limiting alcohol. If attacks are frequent or severe, consult a rheumatologist for uric acid-lowering medications."
                }
            ]
        },
        {
            "name": "Panic Disorder",
            "variations": [
                {
                    "group": "Adults (20-50)",
                    "prompts": [
                        "I have sudden episodes of intense fear with racing heart and sweating.",
                        "What are panic attack symptoms?",
                        "I feel like I'm having a heart attack but tests are normal.",
                        "I have overwhelming fear that comes out of nowhere.",
                        "I get short of breath and feel like I'm dying during anxiety episodes.",
                        "I avoid places where I've had panic attacks before.",
                        "I have chest pain and dizziness with intense fear."
                    ],
                    "completion": "Sudden episodes of intense fear with physical symptoms like racing heart, sweating, shortness of breath, and chest pain suggest panic disorder. During an attack, practice deep breathing, remind yourself it will pass (usually peaks within 10 minutes), and use grounding techniques. Avoid caffeine and alcohol, which can trigger attacks. If panic attacks are frequent, interfere with daily life, or cause avoidance behaviors, consult a mental health professional. Cognitive-behavioral therapy and sometimes medication are very effective treatments."
                }
            ]
        },
        {
            "name": "Chronic Kidney Disease",
            "variations": [
                {
                    "group": "Adults with Diabetes/Hypertension (45-75)",
                    "prompts": [
                        "I have diabetes and recently noticed swelling in my legs.",
                        "What are early kidney disease symptoms?",
                        "I have high blood pressure and my urine is foamy.",
                        "I feel tired and have lost my appetite lately.",
                        "I have diabetes and my doctor mentioned kidney function concerns."
                    ],
                    "completion": "Leg swelling, foamy urine, fatigue, and loss of appetite in someone with diabetes or hypertension may indicate chronic kidney disease. Early stages often have no symptoms, making regular screening important for high-risk individuals. Management focuses on controlling underlying conditions (diabetes, blood pressure), limiting protein intake if advised, avoiding nephrotoxic medications, and regular monitoring of kidney function. If kidney disease progresses, specialized care from a nephrologist is needed for treatment planning and potential preparation for dialysis or transplantation."
                }
            ]
        },
        {
            "name": "Osteoporosis",
            "variations": [
                {
                    "group": "Postmenopausal Women (50+)",
                    "prompts": [
                        "I'm postmenopausal and worried about bone health.",
                        "What are osteoporosis symptoms?",
                        "I had a fracture from a minor fall.",
                        "How do you prevent bone loss after menopause?",
                        "I'm getting shorter and have back pain."
                    ],
                    "completion": "Postmenopausal women are at high risk for osteoporosis due to estrogen decline. Often the first sign is a fracture from minor trauma. Prevention includes adequate calcium (1200mg daily) and vitamin D (800-1000 IU), weight-bearing exercise, avoiding smoking and excessive alcohol, and fall prevention. Bone density screening (DEXA scan) is recommended for women over 65 or postmenopausal women with risk factors. If osteoporosis is diagnosed, medications like bisphosphonates may be prescribed to prevent fractures."
                }
            ]
        },
        {
            "name": "Atrial Fibrillation",
            "variations": [
                {
                    "group": "Adults (50-80)",
                    "prompts": [
                        "I feel like my heart is racing and beating irregularly.",
                        "What are atrial fibrillation symptoms?",
                        "I have palpitations and feel short of breath.",
                        "How serious is irregular heartbeat?",
                        "My heart feels like it's fluttering in my chest.",
                        "I have chest discomfort with irregular pulse.",
                        "I feel weak and dizzy with heart palpitations."
                    ],
                    "completion": "Heart palpitations with irregular rhythm, especially if persistent, may indicate atrial fibrillation (AFib), requiring immediate medical evaluation. AFib increases stroke risk significantly due to blood clot formation. Seek prompt medical attention for heart rhythm evaluation with ECG. Treatment may include rate control medications, blood thinners to prevent stroke, and sometimes rhythm control procedures. Lifestyle modifications include limiting caffeine/alcohol, managing blood pressure, and treating sleep apnea if present. Never ignore persistent irregular heartbeat - contact your cardiologist or emergency services."
                }
            ]
        },
        {
        "name": "Glaucoma",
        "variations": [
            {
                "group": "Elderly",
                "prompts": [
                    "I feel like I'm losing my side vision. Could it be glaucoma?",
                    "What are the symptoms of glaucoma?",
                    "How is glaucoma treated?"
                ],
                "completion": "Glaucoma is a disease that damages the optic nerve, often causing gradual peripheral vision loss. It requires diagnosis by an ophthalmologist and is typically managed with medicated eye drops or surgery to lower eye pressure."
            }
        ]
    },
    {
        "name": "Cataracts",
        "variations": [
            {
                "group": "Elderly",
                "prompts": [
                    "My vision is getting blurry and cloudy, like looking through a foggy window. Is this a cataract?",
                    "What causes cloudy vision in older adults?",
                    "How are cataracts fixed?"
                ],
                "completion": "Cataracts are a common condition where the lens of the eye becomes cloudy, causing blurry vision. The only effective treatment is a routine surgical procedure performed by an ophthalmologist to replace the cloudy lens."
            }
        ]
    },
    {
        "name": "Age-Related Macular Degeneration (AMD)",
        "variations": [
            {
                "group": "Elderly",
                "prompts": [
                    "The center of my vision is becoming blurry and straight lines look wavy. Is this AMD?",
                    "What are the symptoms of macular degeneration?",
                    "How is AMD managed?"
                ],
                "completion": "AMD affects central vision, making tasks like reading difficult. An ophthalmologist can diagnose it and may recommend treatments like specialized vitamin supplements or eye injections to slow its progression."
            }
        ]
    },
    {
        "name": "Dry Eye Syndrome",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "My eyes constantly feel gritty, burning, and dry. What could this be?",
                    "What are the symptoms of dry eye syndrome?",
                    "How can I treat my dry eyes?"
                ],
                "completion": "Dry eye syndrome occurs when your eyes don't produce enough quality tears. Over-the-counter artificial tears can provide relief, but a consultation with an eye doctor is recommended for proper diagnosis and treatment."
            }
        ]
    },

    # --- Teeth & Oral Diseases ---
    {
        "name": "Dental Caries (Cavities)",
        "variations": [
            {
                "group": "Adult/Child",
                "prompts": [
                    "I have sharp pain in a tooth when I eat something sweet or cold. Is this a cavity?",
                    "What are the signs of a cavity?",
                    "How are cavities fixed?"
                ],
                "completion": "A cavity is a permanently damaged area in a tooth that develops into a tiny hole. It is caused by tooth decay and must be treated by a dentist, who will typically remove the decay and place a filling."
            }
        ]
    },
    {
        "name": "Gingivitis",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "My gums are red, swollen, and bleed easily when I brush them. Is this gingivitis?",
                    "What are the symptoms of early gum disease?",
                    "How do you treat inflamed gums?"
                ],
                "completion": "Gingivitis is the initial stage of gum disease caused by plaque buildup. It is reversible with improved oral hygiene (brushing and flossing) and a professional cleaning from a dentist or dental hygienist."
            }
        ]
    },
    {
        "name": "Periodontitis",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "My gums are pulling away from my teeth and my teeth feel loose. Could it be periodontitis?",
                    "What are the symptoms of advanced gum disease?",
                    "How is serious gum disease treated?"
                ],
                "completion": "Periodontitis is a serious gum infection that damages the soft tissue and bone that support your teeth. It is not reversible at home and requires immediate professional treatment by a dentist or periodontist to prevent tooth loss."
            }
        ]
    },
    {
        "name": "Tooth Abscess",
        "variations": [
            {
                "group": "Adult",
                "prompts": [
                    "I have a severe, throbbing toothache and swelling in my jaw. Is it an abscess?",
                    "What are the signs of an infected tooth?",
                    "What should I do for a severe toothache with swelling?"
                ],
                "completion": "An abscess is a pocket of pus caused by a bacterial infection in a tooth. This is a serious condition that requires urgent dental care. A dentist must drain the abscess and treat the infection to prevent it from spreading."
            }
        ]
    },
    {
        "name": "Morning Sickness (Nausea and Vomiting of Pregnancy)",
        "variations": [
            {
                "group": "Pregnant",
                "prompts": [
                    "I'm 8 weeks pregnant and feel nauseous all day. How can I manage this?",
                    "What is morning sickness?",
                    "How do you treat nausea during pregnancy?"
                ],
                "completion": "Nausea, with or without vomiting, is very common in early pregnancy. Eating small, frequent meals and trying ginger or vitamin B6 can help. If you're unable to keep any food or fluids down, it's essential to contact your healthcare provider."
            }
        ]
    },
    {
        "name": "Fatigue in Pregnancy",
        "variations": [
            {
                "group": "Pregnant",
                "prompts": [
                    "I'm in my first trimester and feel exhausted all the time. Is this normal?",
                    "What causes extreme fatigue in early pregnancy?",
                    "How can I cope with pregnancy fatigue?"
                ],
                "completion": "Extreme fatigue is a very common symptom, especially in the first and third trimesters, due to hormonal changes. Prioritizing rest is key. However, mention this to your doctor to rule out other issues like anemia."
            }
        ]
    },

    # --- Common Second/Third Trimester Discomforts ---
    {
        "name": "Round Ligament Pain",
        "variations": [
            {
                "group": "Pregnant",
                "prompts": [
                    "I get a sharp, sudden pain in my lower belly when I stand up or roll over. What is this?",
                    "What does round ligament pain feel like?",
                    "Is a sharp jabbing pain in the abdomen normal during pregnancy?"
                ],
                "completion": "This sounds like round ligament pain, caused by the stretching of ligaments supporting the uterus. It's common and harmless. Moving slowly can help. Always consult your provider for any pain that is severe or persistent to rule out other causes."
            }
        ]
    },
    {
        "name": "Heartburn (Acid Reflux) in Pregnancy",
        "variations": [
            {
                "group": "Pregnant",
                "prompts": [
                    "I have a painful burning sensation in my chest after eating. How can I fix this?",
                    "What causes heartburn during pregnancy?",
                    "Is it safe to take antacids while pregnant?"
                ],
                "completion": "Heartburn is common in pregnancy due to hormonal changes. Eating smaller meals and avoiding trigger foods can help. Before taking any over-the-counter medication, you must discuss safe options with your OB/GYN or midwife."
            }
        ]
    },
    {
        "name": "Swelling (Edema) in Pregnancy",
        "variations": [
            {
                "group": "Pregnant",
                "prompts": [
                    "My feet and ankles are very swollen at the end of the day. Is this normal?",
                    "What causes swelling in pregnancy?",
                    "How can I reduce swelling in my legs and feet?"
                ],
                "completion": "Mild swelling (edema) in the feet and ankles is normal. Elevating your feet and staying hydrated can help. However, sudden or excessive swelling, especially in the hands or face, must be reported to your doctor immediately as it can be a sign of preeclampsia."
            }
        ]
    },

    # --- Serious Pregnancy Complications ---
    {
        "name": "Preeclampsia",
        "variations": [
            {
                "group": "Pregnant",
                "prompts": [
                    "I have a severe headache, vision changes, and sudden swelling. What could this be?",
                    "What are the warning signs of preeclampsia?",
                    "What should I do if I think I have preeclampsia?"
                ],
                "completion": "Preeclampsia is a serious blood pressure disorder. Symptoms like a severe headache, vision disturbances, and sudden swelling require immediate medical attention. Contact your doctor or go to the hospital right away."
            }
        ]
    },
    {
        "name": "Gestational Diabetes",
        "variations": [
            {
                "group": "Pregnant",
                "prompts": [
                    "I was just diagnosed with gestational diabetes. What does this mean?",
                    "How is gestational diabetes managed?",
                    "What are the risks of having diabetes during pregnancy?"
                ],
                "completion": "Gestational diabetes is high blood sugar that develops during pregnancy. It is managed under a doctor's care through diet, exercise, and blood sugar monitoring. Following your healthcare team's plan is crucial for a healthy pregnancy."
            }
        ]
    },
    {
        "name": "Placenta Previa",
        "variations": [
            {
                "group": "Pregnant",
                "prompts": [
                    "I'm in my second trimester and experiencing painless, bright red bleeding. What could cause this?",
                    "What is placenta previa?",
                    "How is placenta previa managed?"
                ],
                "completion": "Painless vaginal bleeding can be a sign of placenta previa, where the placenta covers the cervix. Any bleeding during pregnancy requires an immediate call to your doctor or midwife for evaluation and a management plan."
            }
        ]
    },
    {
        "name": "Anemia in Pregnancy",
        "variations": [
            {
                "group": "Pregnant",
                "prompts": [
                    "I'm pregnant and feel extremely weak, dizzy, and short of breath. Could I be anemic?",
                    "What are the symptoms of iron-deficiency anemia in pregnancy?",
                    "How is anemia during pregnancy treated?"
                ],
                "completion": "Iron-deficiency anemia is common in pregnancy and can cause severe fatigue and dizziness. Your doctor can confirm this with a blood test and will likely recommend an iron supplement. Do not take supplements without medical advice."
            }
        ]
    },

    # --- Labor and Delivery Topics ---
    {
        "name": "Preterm Labor",
        "variations": [
            {
                "group": "Pregnant",
                "prompts": [
                    "I'm 34 weeks and having regular, painful contractions every 10 minutes. Is this preterm labor?",
                    "What are the signs of premature labor?",
                    "What should I do if I think I'm in labor too early?"
                ],
                "completion": "Signs of preterm labor include regular contractions, constant lower backache, or a change in vaginal discharge. If you experience these symptoms before 37 weeks, you must contact your healthcare provider or go to the hospital immediately."
            }
        ]
    },
    {
        "name": "Braxton Hicks Contractions",
        "variations": [
            {
                "group": "Pregnant",
                "prompts": [
                    "My stomach keeps getting hard and tight, but it's not painful and irregular. Is this labor?",
                    "What's the difference between Braxton Hicks and real labor?",
                    "What do Braxton Hicks contractions feel like?"
                ],
                "completion": "These sound like Braxton Hicks contractions, which are irregular 'practice' contractions. They are normal and don't cause labor. If contractions become regular, stronger, and closer together, you should call your doctor or midwife."
            }
        ]
    },

    # --- Postpartum Conditions ---
    {
        "name": "Postpartum Depression (PPD)",
        "variations": [
            {
                "group": "Postpartum",
                "prompts": [
                    "I had a baby weeks ago and feel constantly sad, anxious, and overwhelmed. Is this PPD?",
                    "How is postpartum depression different from the 'baby blues'?",
                    "How can I get help for PPD?"
                ],
                "completion": "Postpartum depression is a serious medical condition involving intense feelings of sadness and anxiety that interfere with daily care. It's more severe and lasts longer than the 'baby blues.' It is treatable and essential to speak with your healthcare provider for support and treatment."
            }
        ]
    },
    # --- Common Childhood Illnesses ---
    {
        "name": "Stomach Flu (Gastroenteritis)",
        "variations": [
            {
                "group": "Child",
                "prompts": [
                    "My child is vomiting and has diarrhea. What should I do?",
                    "What are the symptoms of stomach flu in kids?",
                    "How do I keep my kid hydrated when they are sick?"
                ],
                "completion": "Gastroenteritis is a common viral illness. The main goal is to prevent dehydration by offering small, frequent sips of water or an electrolyte solution. It's crucial to call a pediatrician if your child shows signs of dehydration, like a dry mouth, no tears, or not urinating for many hours."
            }
        ]
    },
    {
        "name": "Hand, Foot, and Mouth Disease",
        "variations": [
            {
                "group": "Toddler/Child",
                "prompts": [
                    "My toddler has a rash on her hands and feet and sores in her mouth. What is this?",
                    "What are the signs of hand, foot, and mouth disease?",
                    "How do you treat hand, foot, and mouth disease?"
                ],
                "completion": "This sounds like Hand, Foot, and Mouth Disease, a very contagious but typically mild viral illness common in young children. Focus on comfort care and fluids. You should consult a pediatrician for a formal diagnosis and to rule out other conditions."
            }
        ]
    },
    {
        "name": "Strep Throat",
        "variations": [
            {
                "group": "Child",
                "prompts": [
                    "My child has a very sudden sore throat and a fever. Could it be strep?",
                    "What are the symptoms of strep throat vs. a regular sore throat?",
                    "Why is it important to see a doctor for a sore throat?"
                ],
                "completion": "Strep throat is a bacterial infection that causes a sudden, severe sore throat, pain with swallowing, and fever. Unlike a cold, it requires antibiotics prescribed by a doctor. A pediatrician needs to perform a test to diagnose it correctly."
            }
        ]
    },
    {
        "name": "Pink Eye (Conjunctivitis)",
        "variations": [
            {
                "group": "Child",
                "prompts": [
                    "My child's eye is red, goopy, and stuck shut in the morning. Is this pink eye?",
                    "What causes pink eye in kids?",
                    "How is pink eye treated?"
                ],
                "completion": "Pink eye (conjunctivitis) is an inflammation of the outer layer of the eye. It can be viral or bacterial. Bacterial pink eye often requires antibiotic eye drops, so it's important to have a pediatrician diagnose the cause and prescribe the correct treatment."
            }
        ]
    },
    {
        "name": "Ear Infection (Otitis Media)",
        "variations": [
            {
                "group": "Toddler/Child",
                "prompts": [
                    "My toddler is pulling on his ear and is very fussy with a fever. Could it be an ear infection?",
                    "What are the signs of an ear infection?",
                    "Do all ear infections need antibiotics?"
                ],
                "completion": "Fever, ear pulling, and fussiness are classic signs of a middle ear infection. A pediatrician needs to look inside the ear to diagnose it properly and decide if antibiotics are necessary, as not all cases require them."
            }
        ]
    },

    # --- Common Injuries ---
    {
        "name": "Concussion",
        "variations": [
            {
                "group": "Child",
                "prompts": [
                    "My child hit their head and now seems confused and dizzy. Could it be a concussion?",
                    "What are the signs of a concussion in a child?",
                    "What should I do if I think my kid has a concussion?"
                ],
                "completion": "A concussion is a mild brain injury. Symptoms include headache, confusion, dizziness, and nausea. Any child suspected of having a concussion needs to be evaluated by a healthcare professional immediately to determine the severity and a safe plan for recovery."
            }
        ]
    },
    {
        "name": "Minor Cuts and Scrapes",
        "variations": [
            {
                "group": "Child",
                "prompts": [
                    "How should I clean my child's scraped knee?",
                    "What's the best way to care for a minor cut?",
                    "When does a cut need stitches?"
                ],
                "completion": "For minor cuts and scrapes, gently clean the area with soap and water, apply an antibiotic ointment, and cover with a bandage. You should see a doctor if the cut is deep, won't stop bleeding, or shows signs of infection like redness and pus."
            }
        ]
    },
    
    # --- Developmental & Other Topics ---
    {
        "name": "Growing Pains",
        "variations": [
            {
                "group": "Child",
                "prompts": [
                    "My child wakes up at night crying that their legs hurt. Could it be growing pains?",
                    "What are growing pains?",
                    "How can I help my child's leg pain at night?"
                ],
                "completion": "Growing pains are typically an aching or throbbing in the legs of school-aged children, often occurring at night. Gentle massage and warmth can help. It's important to see a pediatrician to rule out other causes, especially if the pain is in one leg, persists during the day, or causes a limp."
            }
        ]
    },
    {
        "name": "Eczema (Atopic Dermatitis)",
        "variations": [
            {
                "group": "Child/Infant",
                "prompts": [
                    "My baby has patches of red, dry, and very itchy skin. Is this eczema?",
                    "What causes eczema flare-ups in kids?",
                    "How do I treat my child's eczema?"
                ],
                "completion": "Eczema is a common skin condition causing dry, itchy, and inflamed skin. Management involves using gentle, fragrance-free moisturizers and avoiding triggers. A pediatrician or dermatologist can provide a diagnosis and prescribe medicated creams for flare-ups."
            }
        ]
    },
    {
        "name": "ADHD (Attention-Deficit/Hyperactivity Disorder)",
        "variations": [
            {
                "group": "Child",
                "prompts": [
                    "My child can't sit still, has trouble focusing in school, and is very impulsive. Could it be ADHD?",
                    "What are the signs of ADHD in a school-aged child?",
                    "How is ADHD diagnosed and managed?"
                ],
                "completion": "ADHD is a neurodevelopmental disorder characterized by patterns of inattention and/or hyperactivity-impulsivity. A proper diagnosis requires a comprehensive evaluation by a qualified healthcare professional, such as a pediatrician or child psychologist. Management often involves therapy, school support, and sometimes medication."
            }
        ]
    },
    {
            "name": "Ear Infection (Otitis Media)",
            "variations": [
                {
                    "group": "Children (6 months - 6 years)",
                    "prompts": [
                        "My child is pulling at their ear and crying, especially at night.",
                        "What are ear infection symptoms in toddlers?",
                        "My baby has fever and keeps touching their ear.",
                        "My child says their ear hurts and has trouble hearing.",
                        "My toddler is fussy and has drainage from their ear.",
                        "My child had a cold and now their ear hurts."
                    ],
                    "completion": "Ear pulling, crying (especially at night), fever, and hearing changes in young children suggest ear infection (otitis media). Children are more prone to ear infections due to shorter, more horizontal ear tubes. Pain management includes acetaminophen or ibuprofen for children over 6 months. Warm compresses may provide comfort. Most infections are viral and resolve on their own, but see your pediatrician for proper diagnosis. Antibiotics may be needed for bacterial infections or if symptoms are severe. Seek immediate care if child has high fever, severe pain, or drainage from ear."
                },
                {
                    "group": "Adults (18-65)",
                    "prompts": [
                        "I have ear pain and feel like my ear is plugged.",
                        "Can adults get ear infections?",
                        "I have hearing loss and ear pain after swimming.",
                        "My ear hurts and I have discharge coming out."
                    ],
                    "completion": "Adults can develop ear infections, often following upper respiratory infections or water exposure (swimmer's ear). Symptoms include ear pain, feeling of fullness, hearing changes, and sometimes discharge. Outer ear infections (otitis externa) often result from water exposure, while middle ear infections may follow colds. Treatment depends on location and cause - may include antibiotic drops, oral antibiotics, or anti-inflammatory medications. Keep ears dry and avoid inserting objects. If severe pain, fever, or hearing loss occurs, see your healthcare provider promptly."
                }
            ]
        },
        {
            "name": "Tinnitus (Ringing in Ears)",
            "variations": [
                {
                    "group": "Adults (40-70)",
                    "prompts": [
                        "I have constant ringing in my ears that won't stop.",
                        "What causes tinnitus?",
                        "I hear buzzing sounds when everything is quiet.",
                        "How do you treat ringing in the ears?",
                        "I have high-pitched sounds in my ears all the time.",
                        "The ringing in my ears is affecting my sleep and concentration."
                    ],
                    "completion": "Constant ringing, buzzing, or high-pitched sounds in the ears suggests tinnitus, which can result from hearing loss, ear infections, medications, or underlying health conditions. While there's no cure, management includes avoiding loud noises, managing stress, limiting caffeine/alcohol, using background noise or white noise machines, and treating underlying conditions. Hearing aids may help if hearing loss is present. If tinnitus is sudden, one-sided, or accompanied by hearing loss or dizziness, seek medical evaluation to rule out serious causes."
                }
            ]
        },
        {
            "name": "Hearing Loss",
            "variations": [
                {
                    "group": "Elderly (65+)",
                    "prompts": [
                        "I'm having trouble hearing conversations, especially in noisy places.",
                        "What are signs of hearing loss in seniors?",
                        "I keep asking people to repeat themselves.",
                        "I turn the TV volume up but others say it's too loud.",
                        "I have difficulty hearing high-pitched sounds like women's voices."
                    ],
                    "completion": "Difficulty hearing conversations, especially in background noise, asking for repetition, and turning up volume suggest age-related hearing loss (presbycusis), affecting about 1/3 of adults over 65. While some hearing loss is normal with aging, significant impairment affects quality of life and safety. Treatment options include hearing aids, assistive listening devices, and communication strategies. Regular hearing tests help monitor progression. If hearing loss is sudden, one-sided, or accompanied by ear pain or dizziness, seek medical evaluation to rule out treatable causes."
                }
            ]
        },
        {
            "name": "Nosebleeds (Epistaxis)",
            "variations": [
                {
                    "group": "Children (3-15 years)",
                    "prompts": [
                        "My child gets frequent nosebleeds, especially in winter.",
                        "What causes nosebleeds in kids?",
                        "My child's nose bleeds when they blow it hard.",
                        "How do you stop a nosebleed?",
                        "My child picks their nose and it bleeds often."
                    ],
                    "completion": "Frequent nosebleeds in children are usually due to dry air, nose picking, or minor trauma to delicate nasal tissues. To stop bleeding: have child sit upright, lean slightly forward, pinch soft part of nose for 10-15 minutes continuously. Apply petroleum jelly inside nostrils to prevent drying. Use humidifiers in dry environments and keep fingernails short. Most childhood nosebleeds are harmless. Seek medical attention if bleeding doesn't stop after 20 minutes, occurs after head injury, or if child has frequent severe nosebleeds."
                },
                {
                    "group": "Adults (25-65)",
                    "prompts": [
                        "I get nosebleeds frequently, especially in dry weather.",
                        "What causes adult nosebleeds?",
                        "I'm on blood thinners and have nosebleeds.",
                        "My nose bleeds when I blow it hard."
                    ],
                    "completion": "Adult nosebleeds often result from dry air, nasal irritation, or medications like blood thinners. Most are anterior (front of nose) and can be managed by sitting upright, leaning forward, and applying direct pressure to soft part of nose for 15 minutes. Use saline nasal sprays and humidifiers to prevent drying. If you're on blood-thinning medications, inform your healthcare provider about frequent nosebleeds. Seek emergency care if bleeding is severe, doesn't stop after 20 minutes, or follows head trauma."
                }
            ]
        },
        
        # ORAL/DENTAL CONDITIONS
        {
            "name": "Dental Abscess",
            "variations": [
                {
                    "group": "Adults (25-65)",
                    "prompts": [
                        "I have severe tooth pain with swelling in my gum and face.",
                        "What are dental abscess symptoms?",
                        "I have throbbing tooth pain that keeps me awake at night.",
                        "My face is swollen and I have a bad taste in my mouth.",
                        "I have intense tooth pain with fever and swollen lymph nodes.",
                        "I have a bump on my gum that's painful and draining pus."
                    ],
                    "completion": "Severe, throbbing tooth pain with facial swelling, fever, and bad taste suggests a dental abscess, a serious bacterial infection. This requires urgent dental treatment and often antibiotics. Take over-the-counter pain relievers, rinse with warm salt water, and apply cold compress to reduce swelling. Do not apply heat to the face. See a dentist immediately or go to emergency room if you have difficulty swallowing, breathing problems, or high fever. Dental abscesses can spread to other parts of the body if untreated."
                }
            ]
        },
        {
            "name": "TMJ Disorder",
            "variations": [
                {
                    "group": "Adults (20-50)",
                    "prompts": [
                        "My jaw clicks and pops when I open my mouth.",
                        "What are TMJ symptoms?",
                        "I have jaw pain and difficulty chewing.",
                        "How do you treat TMJ disorder?",
                        "I grind my teeth and now my jaw hurts constantly.",
                        "I can't open my mouth fully and my jaw locks sometimes.",
                        "I have ear pain but my ears are fine - could it be my jaw?"
                    ],
                    "completion": "Jaw clicking, popping, pain, and difficulty chewing suggest temporomandibular joint (TMJ) disorder. Treatment includes avoiding hard/chewy foods, applying ice or heat to the jaw, gentle jaw exercises, stress management to reduce teeth grinding, and over-the-counter pain relievers. If related to teeth grinding, a night guard may help. Avoid extreme jaw movements like wide yawning. Most TMJ disorders improve with conservative treatment. If symptoms persist or jaw locks, consult a dentist or oral surgeon for specialized evaluation and treatment."
                }
            ]
        },
        {
            "name": "Gingivitis",
            "variations": [
                {
                    "group": "Adults (18-65)",
                    "prompts": [
                        "My gums bleed when I brush my teeth.",
                        "What are signs of gum disease?",
                        "I have red, swollen gums that are tender.",
                        "How do you treat gingivitis?",
                        "My gums are inflamed and I have bad breath.",
                        "I notice blood when I floss and my gums hurt."
                    ],
                    "completion": "Bleeding, red, swollen gums that are tender to touch suggest gingivitis, the early stage of gum disease. This is reversible with proper oral hygiene: brush twice daily with fluoride toothpaste, floss daily, use antibacterial mouthwash, and avoid smoking. Professional dental cleaning removes tartar buildup that causes inflammation. Most cases improve within 1-2 weeks of improved oral care. If gums continue bleeding, become more swollen, or you develop loose teeth or persistent bad breath, see your dentist for evaluation and professional treatment."
                }
            ]
        },
        
        # HORMONAL/ENDOCRINE CONDITIONS
        {
            "name": "Hyperthyroidism",
            "variations": [
                {
                    "group": "Women (20-50)",
                    "prompts": [
                        "I'm losing weight despite eating more and feel anxious all the time.",
                        "What are symptoms of overactive thyroid?",
                        "I have rapid heartbeat, sweating, and feel hot all the time.",
                        "I'm always nervous and my hands shake.",
                        "I have increased appetite but keep losing weight.",
                        "I can't sleep and feel jittery with palpitations.",
                        "My eyes look prominent and I feel restless constantly."
                    ],
                    "completion": "Unexplained weight loss despite increased appetite, rapid heartbeat, sweating, anxiety, and heat intolerance suggest hyperthyroidism (overactive thyroid). Other symptoms include tremors, sleep disturbances, and sometimes eye changes. This condition requires medical evaluation with blood tests (TSH, T3, T4) for diagnosis. Treatment may include antithyroid medications, radioactive iodine, or surgery depending on the cause. Untreated hyperthyroidism can lead to serious cardiac complications. Consult an endocrinologist for proper evaluation and treatment planning."
                }
            ]
        },
        {
            "name": "Cushing's Syndrome",
            "variations": [
                {
                    "group": "Adults (30-60)",
                    "prompts": [
                        "I'm gaining weight in my face and abdomen but my arms and legs are thin.",
                        "What are Cushing's syndrome symptoms?",
                        "I have purple stretch marks and easy bruising.",
                        "I have a round face and hump on my back.",
                        "I have high blood sugar and purple skin marks."
                    ],
                    "completion": "Central weight gain with facial rounding, purple stretch marks, easy bruising, and muscle weakness suggest Cushing's syndrome, caused by excess cortisol. This can result from medications (steroids) or tumors affecting hormone production. Associated symptoms include high blood pressure, diabetes, mood changes, and osteoporosis. Diagnosis requires specialized testing of cortisol levels. Treatment depends on the underlying cause and may involve medication adjustments, surgery, or other interventions. Consult an endocrinologist for proper evaluation if you have multiple suggestive symptoms."
                }
            ]
        },
        {
            "name": "Addison's Disease",
            "variations": [
                {
                    "group": "Adults (20-60)",
                    "prompts": [
                        "I'm constantly fatigued and have been losing weight unintentionally.",
                        "I have darkening of my skin and crave salt.",
                        "I feel weak, dizzy, and have low blood pressure.",
                        "I have nausea, vomiting, and abdominal pain with extreme fatigue.",
                        "I have muscle weakness and depression with skin changes."
                    ],
                    "completion": "Extreme fatigue, weight loss, skin darkening (especially in skin folds), salt cravings, and low blood pressure may suggest Addison's disease (adrenal insufficiency). This rare but serious condition involves inadequate cortisol production. Symptoms develop gradually but can lead to life-threatening adrenal crisis. Diagnosis requires specialized hormone testing. Treatment involves hormone replacement therapy with corticosteroids. If you have multiple symptoms, especially with skin darkening or severe fatigue, consult an endocrinologist for evaluation. Seek emergency care for severe weakness, vomiting, or signs of shock."
                }
            ]
        },
        
        # KIDNEY/UROLOGICAL CONDITIONS
        {
            "name": "Kidney Disease (Early Stage)",
            "variations": [
                {
                    "group": "Adults with Risk Factors (45-75)",
                    "prompts": [
                        "I have diabetes and noticed foamy urine lately.",
                        "What are early kidney disease symptoms?",
                        "I have high blood pressure and swelling in my ankles.",
                        "I'm urinating more at night and feel tired constantly.",
                        "I have diabetes and my urine looks bubbly.",
                        "I feel nauseous and have lost my appetite recently."
                    ],
                    "completion": "Foamy urine, ankle swelling, increased nighttime urination, and fatigue in people with diabetes or hypertension may indicate early kidney disease. Often there are no symptoms until advanced stages, making regular screening crucial for high-risk individuals. Management focuses on controlling blood pressure and blood sugar, limiting protein if advised, staying hydrated, and avoiding medications that can harm kidneys. Regular monitoring with blood tests (creatinine, GFR) and urine tests helps track kidney function. Consult a nephrologist if kidney function declines or protein appears in urine."
                }
            ]
        },
        {
            "name": "Overactive Bladder",
            "variations": [
                {
                    "group": "Adults (40-70)",
                    "prompts": [
                        "I have sudden, urgent need to urinate that's hard to control.",
                        "What are overactive bladder symptoms?",
                        "I leak urine when I get a strong urge to go.",
                        "I urinate frequently during the day and night.",
                        "I have to rush to the bathroom and sometimes don't make it.",
                        "I wake up multiple times at night to urinate."
                    ],
                    "completion": "Sudden, strong urges to urinate with frequency, urgency, and possible leakage suggest overactive bladder. Management includes bladder training (scheduled voiding), pelvic floor exercises (Kegels), limiting caffeine and alcohol, maintaining healthy weight, and fluid management. Keep a bladder diary to identify patterns. Medications may help if conservative measures aren't sufficient. If symptoms significantly impact quality of life or you have blood in urine, consult a urologist for evaluation and treatment options."
                }
            ]
        },
        
        # LIVER CONDITIONS
        {
            "name": "Fatty Liver Disease",
            "variations": [
                {
                    "group": "Adults (35-65)",
                    "prompts": [
                        "I'm overweight and my doctor said I have fatty liver.",
                        "What are fatty liver symptoms?",
                        "I have diabetes and elevated liver enzymes.",
                        "How do you treat non-alcoholic fatty liver disease?",
                        "I feel tired and have right upper abdominal discomfort.",
                        "I have metabolic syndrome and liver problems."
                    ],
                    "completion": "Non-alcoholic fatty liver disease (NAFLD) is common in people with obesity, diabetes, or metabolic syndrome. Often there are no symptoms, but some experience fatigue or right upper abdominal discomfort. Management focuses on weight loss (7-10% of body weight), regular exercise, controlling diabetes and cholesterol, and avoiding alcohol. Follow a Mediterranean-style diet rich in fruits, vegetables, and healthy fats. Regular monitoring with blood tests and imaging helps track progression. If liver enzymes remain elevated or liver scarring develops, consult a hepatologist for specialized care."
                }
            ]
        },
        {
            "name": "Hepatitis (Viral)",
            "variations": [
                {
                    "group": "Adults (20-60)",
                    "prompts": [
                        "I have yellowing of my skin and eyes with fatigue.",
                        "What are hepatitis symptoms?",
                        "I have dark urine and pale stools with abdominal pain.",
                        "I feel nauseated and have lost my appetite with yellow skin.",
                        "I have joint pain and fatigue with jaundice.",
                        "I was exposed to hepatitis and feel sick."
                    ],
                    "completion": "Yellowing of skin and eyes (jaundice), dark urine, pale stools, and fatigue suggest viral hepatitis. This liver infection can be caused by hepatitis A, B, or C viruses. Hepatitis A is often food/water-borne, while B and C spread through blood or sexual contact. Treatment is mainly supportive with rest, adequate nutrition, and avoiding alcohol. Some forms require antiviral medications. Seek medical evaluation for proper diagnosis, monitoring, and to prevent transmission to others. Hepatitis B and C can become chronic and require long-term management."
                }
            ]
        },
        
        # BLOOD/HEMATOLOGICAL CONDITIONS
        {
            "name": "Deep Vein Thrombosis (DVT)",
            "variations": [
                {
                    "group": "Adults (30-70)",
                    "prompts": [
                        "I have swelling, pain, and redness in one leg.",
                        "What are blood clot symptoms in the leg?",
                        "My calf is swollen and warm to touch.",
                        "I have leg pain that gets worse when I walk.",
                        "I flew recently and now have leg swelling and pain.",
                        "One leg is much more swollen than the other."
                    ],
                    "completion": "Unilateral leg swelling, pain, warmth, and redness suggest deep vein thrombosis (DVT), a serious condition where blood clots form in deep veins. This is a medical emergency due to risk of pulmonary embolism if clots travel to lungs. Risk factors include prolonged immobility, recent surgery, cancer, or pregnancy. Seek immediate medical attention for evaluation with ultrasound. Treatment typically involves blood-thinning medications. Never massage a suspected DVT. If you develop sudden shortness of breath or chest pain, call 911 immediately as this may indicate pulmonary embolism."
                }
            ]
        },
        {
            "name": "Anemia (General)",
            "variations": [
                {
                    "group": "Adults (18-75)",
                    "prompts": [
                        "I feel weak and tired all the time with pale skin.",
                        "What are anemia symptoms?",
                        "I get short of breath easily and feel dizzy.",
                        "I have fatigue and my fingernails are pale.",
                        "I feel cold all the time and have no energy.",
                        "I have rapid heartbeat and feel weak with exertion."
                    ],
                    "completion": "Persistent fatigue, weakness, pale skin, shortness of breath, and dizziness suggest anemia (low red blood cell count or hemoglobin). Common causes include iron deficiency, vitamin B12 deficiency, chronic disease, or blood loss. Treatment depends on the underlying cause - iron supplements for iron deficiency, B12 injections for pernicious anemia, or treating underlying conditions. Blood tests determine the type and cause of anemia. If severe or accompanied by chest pain, seek prompt medical evaluation. Most types of anemia respond well to appropriate treatment."
                }
            ]
        },
        
        # AUTOIMMUNE/INFLAMMATORY CONDITIONS
        {
            "name": "Inflammatory Bowel Disease (IBD)",
            "variations": [
                {
                    "group": "Young Adults (20-40)",
                    "prompts": [
                        "I have bloody diarrhea with severe abdominal cramping.",
                        "What are Crohn's disease symptoms?",
                        "I have persistent diarrhea with blood and weight loss.",
                        "I have abdominal pain and frequent urgent bowel movements.",
                        "I have mouth ulcers and joint pain with digestive problems.",
                        "I have chronic diarrhea that doesn't respond to typical treatments."
                    ],
                    "completion": "Bloody diarrhea, severe abdominal cramping, weight loss, and urgency suggest inflammatory bowel disease (IBD) - either Crohn's disease or ulcerative colitis. Unlike IBS, IBD involves intestinal inflammation and can cause serious complications. Symptoms may include mouth ulcers, joint pain, and skin problems. This requires immediate gastroenterology evaluation for proper diagnosis with colonoscopy and imaging. Treatment involves anti-inflammatory medications, immunosuppressants, and dietary modifications. Early diagnosis and treatment prevent complications like strictures or bowel perforation."
                }
            ]
        },
        {
            "name": "Multiple Sclerosis (Early)",
            "variations": [
                {
                    "group": "Young Adults (20-40)",
                    "prompts": [
                        "I have numbness and tingling that comes and goes in different body parts.",
                        "What are early MS symptoms?",
                        "I have vision problems and muscle weakness.",
                        "I feel fatigued and have coordination problems.",
                        "I have electric shock sensations and balance issues.",
                        "I have episodes of symptoms that seem to come and go."
                    ],
                    "completion": "Episodic neurological symptoms like numbness, tingling, vision changes, muscle weakness, and coordination problems that come and go may suggest multiple sclerosis (MS), especially in young adults. MS involves immune system attacks on nerve coverings in the brain and spinal cord. Symptoms can affect any part of the nervous system and may remit and relapse. Early diagnosis is important for treatment that can slow disease progression. If you have multiple neurological symptoms, especially if episodic, consult a neurologist for comprehensive evaluation including MRI and other specialized tests."
                }
            ]
        },
        
        # MENTAL HEALTH CONDITIONS (Additional)
        {
            "name": "Bipolar Disorder",
            "variations": [
                {
                    "group": "Young Adults (18-35)",
                    "prompts": [
                        "I have periods of extreme highs and lows in my mood.",
                        "What are bipolar disorder symptoms?",
                        "Sometimes I'm very energetic and don't need sleep, other times I'm severely depressed.",
                        "I have mood swings that last for days or weeks.",
                        "I go through phases of feeling invincible followed by deep depression.",
                        "My family says I have extreme mood changes that affect my behavior."
                    ],
                    "completion": "Distinct periods of elevated mood (mania/hypomania) alternating with depressive episodes suggest bipolar disorder. Manic symptoms include decreased need for sleep, grandiose thoughts, increased energy, risky behavior, and rapid speech. Depressive episodes involve sadness, hopelessness, fatigue, and loss of interest. This serious mental health condition requires professional evaluation and treatment with mood stabilizers, therapy, and lifestyle management. If you experience extreme mood swings or thoughts of self-harm, consult a psychiatrist or mental health professional immediately."
                }
            ]
        },
        {
            "name": "ADHD (Adult)",
            "variations": [
                {
                    "group": "Adults (25-45)",
                    "prompts": [
                        "I have trouble focusing at work and am easily distracted.",
                        "What are adult ADHD symptoms?",
                        "I procrastinate constantly and have trouble organizing tasks.",
                        "I'm impulsive and interrupt people during conversations.",
                        "I lose things frequently and have trouble following instructions.",
                        "I was hyperactive as a child and still have attention problems."
                    ],
                    "completion": "Persistent difficulty with attention, organization, impulsivity, and task completion that interferes with work or relationships may suggest adult ADHD. Many adults are diagnosed later in life when work or family demands exceed their coping abilities. Symptoms include procrastination, disorganization, restlessness, and difficulty sustaining attention. Treatment includes behavioral strategies, organizational tools, and potentially stimulant or non-stimulant medications. If symptoms significantly impact work performance or relationships, consult a psychiatrist or psychologist specializing in adult ADHD for comprehensive evaluation."
                }
            ]
        },
        {
            "name": "PTSD",
            "variations": [
                {
                    "group": "Adults (20-65)",
                    "prompts": [
                        "I experienced trauma and now have nightmares and flashbacks.",
                        "What are PTSD symptoms?",
                        "I avoid places that remind me of a traumatic event.",
                        "I'm easily startled and feel on edge constantly.",
                        "I have intrusive thoughts about a traumatic experience.",
                        "I feel numb emotionally and have trouble sleeping after trauma."
                    ],
                    "completion": "Nightmares, flashbacks, avoidance behaviors, hypervigilance, and emotional numbing following a traumatic event suggest post-traumatic stress disorder (PTSD). This serious mental health condition affects people who have experienced or witnessed trauma. Treatment includes trauma-focused therapy (EMDR, CPT), potentially medications for symptoms, and support groups. PTSD is highly treatable with appropriate care. If you have thoughts of self-harm or substance abuse following trauma, seek immediate mental health care. Contact a trauma specialist or your healthcare provider for proper evaluation and treatment."
                }
            ]
        },
        {
            "name": "Obsessive-Compulsive Disorder (OCD)",
            "variations": [
                {
                    "group": "Adults (18-45)",
                    "prompts": [
                        "I have intrusive thoughts that won't go away and feel compelled to do certain actions.",
                        "What are OCD symptoms?",
                        "I wash my hands repeatedly and check locks multiple times.",
                        "I have unwanted thoughts that cause severe anxiety.",
                        "I spend hours on rituals and can't stop myself.",
                        "I have fears about contamination and clean excessively."
                    ],
                    "completion": "Intrusive, unwanted thoughts (obsessions) that cause anxiety, coupled with repetitive behaviors or mental acts (compulsions) performed to reduce distress, suggest obsessive-compulsive disorder (OCD). Common themes include contamination fears, checking behaviors, or need for symmetry. OCD significantly impacts daily functioning and relationships. Treatment includes cognitive-behavioral therapy (specifically exposure and response prevention), potentially SSRI medications, and support groups. If obsessions or compulsions consume significant time or cause distress, consult a mental health professional specializing in OCD for evaluation and treatment."
                }
            ]
        },
        
        # SLEEP DISORDERS (Additional)
        {
            "name": "Restless Leg Syndrome",
            "variations": [
                {
                    "group": "Adults (40-70)",
                    "prompts": [
                        "I have an irresistible urge to move my legs, especially at night.",
                        "What are restless leg syndrome symptoms?",
                        "My legs feel uncomfortable and I can't keep them still when trying to sleep.",
                        "How do you treat restless legs?",
                        "I have crawling sensations in my legs that are worse in the evening.",
                        "I have to get up and walk around because my legs feel so uncomfortable."
                    ],
                    "completion": "Irresistible urge to move legs with uncomfortable sensations, worse in the evening and temporarily relieved by movement, suggests restless leg syndrome (RLS). Initial management includes regular exercise (but not close to bedtime), avoiding caffeine and alcohol, maintaining consistent sleep schedule, and checking iron levels as deficiency can worsen RLS. Gentle leg massage and warm baths may provide relief. If symptoms significantly disrupt sleep or daily life, consult a neurologist or sleep specialist for evaluation and potential medication treatment."
                }
            ]
        },
        {
            "name": "Narcolepsy",
            "variations": [
                {
                    "group": "Young Adults (15-35)",
                    "prompts": [
                        "I fall asleep suddenly during the day even when I'm not tired.",
                        "What are narcolepsy symptoms?",
                        "I have uncontrollable sleep attacks and muscle weakness with emotions.",
                        "I fall asleep at inappropriate times like during conversations.",
                        "I have vivid dreams when falling asleep and muscle paralysis episodes."
                    ],
                    "completion": "Sudden, uncontrollable sleep episodes during the day, especially with cataplexy (muscle weakness triggered by emotions), suggest narcolepsy, a neurological sleep disorder. Other symptoms include vivid hallucinations when falling asleep/waking up and sleep paralysis. This condition significantly impacts daily functioning and safety. Diagnosis requires sleep studies and specialized testing. Treatment includes stimulant medications, scheduled naps, good sleep hygiene, and lifestyle modifications. If you experience sudden sleep attacks or muscle weakness with laughter/emotions, consult a sleep specialist for evaluation."
                }
            ]
        },
        
        # CANCER SCREENING/EARLY DETECTION
        {
            "name": "Skin Cancer (Early Detection)",
            "variations": [
                {
                    "group": "Adults (30-70)",
                    "prompts": [
                        "I have a mole that has changed color and shape.",
                        "What are signs of skin cancer?",
                        "I have a spot on my skin that bleeds and won't heal.",
                        "How do you check for melanoma?",
                        "I have a new growth that looks different from my other moles.",
                        "I have a mole that's asymmetrical and has irregular borders."
                    ],
                    "completion": "Changes in moles or new skin growths require evaluation using the ABCDE criteria: Asymmetry, Border irregularity, Color variation, Diameter >6mm, and Evolving (changing). Any mole that bleeds, itches, or doesn't heal should be examined. Risk factors include fair skin, sun exposure history, family history, and multiple moles. Perform monthly self-examinations and have annual professional skin checks if at high risk. If you notice suspicious changes, see a dermatologist promptly. Early detection of skin cancer leads to excellent treatment outcomes."
                }
            ]
        },
        {
            "name": "Breast Health Concerns",
            "variations": [
                {
                    "group": "Women (25-65)",
                    "prompts": [
                        "I found a lump in my breast during self-examination.",
                        "What are breast cancer warning signs?",
                        "I have breast pain and tenderness before my period.",
                        "I noticed changes in breast size or shape.",
                        "I have nipple discharge that's not related to breastfeeding.",
                        "I have dimpling or puckering of breast skin."
                    ],
                    "completion": "Any breast lump, changes in size/shape, skin dimpling, or nipple discharge requires medical evaluation, though most breast lumps are benign. Perform monthly self-exams and report changes to your healthcare provider. Cyclical breast tenderness before periods is usually normal (fibrocystic changes). Follow mammography guidelines starting at age 40-50. If you have family history of breast/ovarian cancer, discuss earlier screening and genetic testing. Any persistent breast changes warrant clinical breast examination and possibly imaging studies."
                }
            ]
        },
        
        # INFECTIOUS DISEASES (Additional)
        {
            "name": "Mononucleosis (Mono)",
            "variations": [
                {
                    "group": "Teenagers/Young Adults (15-25)",
                    "prompts": [
                        "I have severe fatigue, sore throat, and swollen lymph nodes.",
                        "What are mono symptoms?",
                        "I'm exhausted and have been sick for weeks.",
                        "I have a sore throat that won't go away and feel very tired.",
                        "I have fever, body aches, and enlarged glands in my neck.",
                        "I can barely stay awake and my throat hurts constantly."
                    ],
                    "completion": "Severe fatigue lasting weeks, persistent sore throat, and swollen lymph nodes in teenagers or young adults suggest mononucleosis (mono), often caused by Epstein-Barr virus. Treatment is supportive: rest, adequate fluids, pain relievers for throat pain, and avoiding contact sports due to spleen enlargement risk. Most people recover in 2-4 weeks, though fatigue may persist longer. Seek medical attention if you develop severe throat pain affecting swallowing, difficulty breathing, or signs of dehydration. Blood tests can confirm diagnosis."
                }
            ]
        },
        {
            "name": "Lyme Disease",
            "variations": [
                {
                    "group": "Adults (All Ages)",
                    "prompts": [
                        "I have a bull's-eye rash after being in wooded areas.",
                        "What are Lyme disease symptoms?",
                        "I have flu-like symptoms and joint pain after a tick bite.",
                        "I found a tick on me and now have a spreading rash.",
                        "I have fatigue, muscle aches, and a circular rash.",
                        "I was hiking and now have fever and joint pain."
                    ],
                    "completion": "A bull's-eye rash (erythema migrans) after outdoor exposure in tick-endemic areas strongly suggests Lyme disease. Early symptoms include flu-like illness, fatigue, muscle aches, and joint pain. Early treatment with antibiotics (doxycycline) is highly effective and prevents progression to chronic Lyme disease. If you find an attached tick, remove it promptly with tweezers and save it for identification. Seek medical attention if you develop a rash or flu-like symptoms after tick exposure, especially in areas known for Lyme disease."
                }
            ]
        },
        
        # NUTRITIONAL DEFICIENCIES
        {
            "name": "Vitamin B12 Deficiency",
            "variations": [
                {
                    "group": "Vegetarians/Vegans (25-65)",
                    "prompts": [
                        "I'm vegetarian and have fatigue with numbness in my hands and feet.",
                        "What are B12 deficiency symptoms?",
                        "I have memory problems and feel tired constantly.",
                        "I'm vegan and have been feeling weak and confused.",
                        "I have pale skin and my tongue feels sore.",
                        "I have balance problems and mood changes."
                    ],
                    "completion": "Fatigue, numbness/tingling in hands and feet, memory problems, and pale skin in vegetarians/vegans suggest vitamin B12 deficiency. B12 is primarily found in animal products, making plant-based dieters at risk. Symptoms can include neurological problems, anemia, and mood changes. Treatment involves B12 supplements or injections, and increasing fortified foods. Neurological symptoms may be irreversible if deficiency is prolonged. Regular B12 monitoring is recommended for those following plant-based diets. Consult your healthcare provider for testing and appropriate supplementation."
                }
            ]
        },
        {
            "name": "Folate Deficiency",
            "variations": [
                {
                    "group": "Pregnant Women",
                    "prompts": [
                        "I'm pregnant and feel very tired with pale skin.",
                        "What are folate deficiency symptoms during pregnancy?",
                        "I have anemia and my doctor mentioned folate levels.",
                        "I'm expecting and have mouth sores with fatigue."
                    ],
                    "completion": "Fatigue, pale skin, and anemia during pregnancy may indicate folate deficiency, crucial for preventing birth defects. Folate needs increase significantly during pregnancy for fetal neural tube development. Symptoms include fatigue, pale skin, mouth sores, and irritability. All pregnant women should take prenatal vitamins containing at least 400-600 mcg of folic acid. Increase folate-rich foods like leafy greens, citrus fruits, and fortified grains. If deficiency is diagnosed, higher dose supplements may be needed. Consult your obstetrician about appropriate folate supplementation."
                }
            ]
        },
        
        # EYE CONDITIONS (Additional)
        {
            "name": "Dry Eye Syndrome",
            "variations": [
                {
                    "group": "Adults (40-70)",
                    "prompts": [
                        "My eyes feel dry, gritty, and burn constantly.",
                        "What causes dry eyes?",
                        "I have eye irritation and my vision is sometimes blurry.",
                        "How do you treat chronic dry eyes?",
                        "My eyes water excessively but still feel dry.",
                        "I have eye discomfort that's worse in air conditioning or wind."
                    ],
                    "completion": "Gritty, burning eyes with blurred vision and paradoxical tearing suggest dry eye syndrome, common with aging, certain medications, or environmental factors. Treatment includes artificial tears (preservative-free for frequent use), warm compresses, omega-3 supplements, and environmental modifications (humidifiers, avoiding direct air flow). Computer users should follow the 20-20-20 rule and blink frequently. If symptoms persist despite over-the-counter treatments or significantly impact daily activities, consult an ophthalmologist for prescription treatments or procedures."
                }
            ]
        },
        {
            "name": "Glaucoma",
            "variations": [
                {
                    "group": "Adults (50+)",
                    "prompts": [
                        "I have gradual vision loss starting from the edges.",
                        "What are glaucoma symptoms?",
                        "I have increased eye pressure and family history of glaucoma.",
                        "I have headaches and see halos around lights.",
                        "I'm losing peripheral vision but central vision is okay."
                    ],
                    "completion": "Gradual peripheral vision loss, especially with family history or increased eye pressure, suggests glaucoma, the 'silent thief of sight.' Early stages often have no symptoms, making regular eye exams crucial for adults over 40 (or younger with risk factors). Treatment involves eye drops to lower pressure, and sometimes laser or surgical procedures. Once vision is lost to glaucoma, it cannot be restored, making early detection and treatment critical. If you have family history, are African American, or over 60, ensure regular comprehensive eye exams."
                }
            ]
        },
        {
            "name": "Cataracts",
            "variations": [
                {
                    "group": "Elderly (60+)",
                    "prompts": [
                        "My vision is cloudy and I have trouble seeing at night.",
                        "What are cataract symptoms?",
                        "I see halos around lights and have increased glare sensitivity.",
                        "My vision seems foggy and colors appear faded.",
                        "I need brighter light to read and have trouble with night driving."
                    ],
                    "completion": "Cloudy, foggy vision with increased glare sensitivity, halos around lights, and difficulty with night vision suggest cataracts, clouding of the eye's natural lens. This is common with aging and develops gradually. Early stages may be managed with stronger lighting, anti-glare sunglasses, and updated prescriptions. When cataracts significantly impact daily activities or safety (especially driving), surgical replacement with artificial lens is highly successful. Most people achieve excellent vision improvement after cataract surgery. Consult an ophthalmologist for evaluation and surgical planning when vision problems interfere with quality of life."
                }
            ]
        },
        
        # DIGESTIVE CONDITIONS (Additional)
        {
            "name": "Peptic Ulcer Disease",
            "variations": [
                {
                    "group": "Adults (30-65)",
                    "prompts": [
                        "I have burning stomach pain that's worse when my stomach is empty.",
                        "What are stomach ulcer symptoms?",
                        "I have pain between meals that improves when I eat.",
                        "I have stomach pain with nausea and feel full quickly.",
                        "I have burning pain in my upper abdomen that wakes me at night.",
                        "I take a lot of ibuprofen and now have stomach pain."
                    ],
                    "completion": "Burning stomach pain that's worse on an empty stomach and improves with eating suggests peptic ulcer disease. Common causes include H. pylori bacterial infection and long-term use of NSAIDs (ibuprofen, aspirin). Treatment involves proton pump inhibitors to reduce acid, antibiotics if H. pylori is present, and avoiding NSAIDs and alcohol. Eat smaller, frequent meals and manage stress. Seek immediate medical attention if you have severe abdominal pain, vomiting blood, or black, tarry stools, as these may indicate bleeding ulcers requiring emergency treatment."
                }
            ]
        },
        {
            "name": "Lactose Intolerance",
            "variations": [
                {
                    "group": "Adults (All Ages)",
                    "prompts": [
                        "I have bloating, gas, and diarrhea after drinking milk.",
                        "What are lactose intolerance symptoms?",
                        "I get stomach cramps when I eat dairy products.",
                        "How do you manage lactose intolerance?",
                        "I have digestive problems but only after eating ice cream or cheese.",
                        "I feel nauseous and gassy after consuming dairy."
                    ],
                    "completion": "Bloating, gas, diarrhea, and stomach cramps specifically after consuming dairy products suggest lactose intolerance, the inability to digest lactose (milk sugar). Management includes limiting or avoiding dairy products, using lactase enzyme supplements before consuming dairy, choosing lactose-free alternatives, and gradually introducing small amounts of dairy to determine tolerance levels. Hard cheeses and yogurt are often better tolerated. If symptoms are severe or you're unsure about the diagnosis, consult your healthcare provider for testing and dietary guidance."
                }
            ]
        },
        {
            "name": "Celiac Disease",
            "variations": [
                {
                    "group": "Adults (20-60)",
                    "prompts": [
                        "I have chronic diarrhea, weight loss, and abdominal pain.",
                        "What are celiac disease symptoms?",
                        "I feel bloated and tired after eating bread or pasta.",
                        "I have digestive problems that seem related to gluten.",
                        "I have anemia and digestive issues with weight loss.",
                        "I have skin rash and digestive problems after eating wheat."
                    ],
                    "completion": "Chronic diarrhea, weight loss, abdominal pain, and bloating after consuming gluten-containing foods (wheat, barley, rye) suggest celiac disease, an autoimmune condition. Other symptoms include fatigue, anemia, skin rash (dermatitis herpetiformis), and nutrient deficiencies. Diagnosis requires blood tests for specific antibodies and intestinal biopsy while still consuming gluten. Treatment is strict, lifelong gluten-free diet. With proper diet adherence, intestinal healing occurs and symptoms resolve. If you suspect celiac disease, consult a gastroenterologist for proper testing before starting a gluten-free diet."
                }
            ]
        },
        
        # AUTOIMMUNE CONDITIONS (Additional)
        {
            "name": "Hashimoto's Thyroiditis",
            "variations": [
                {
                    "group": "Women (30-60)",
                    "prompts": [
                        "I have hypothyroid symptoms and my doctor mentioned Hashimoto's.",
                        "What is Hashimoto's thyroiditis?",
                        "I have fatigue, weight gain, and thyroid antibodies.",
                        "I have an enlarged thyroid gland and feel tired constantly.",
                        "I have autoimmune thyroid disease with fluctuating symptoms."
                    ],
                    "completion": "Hashimoto's thyroiditis is an autoimmune condition where the immune system attacks the thyroid gland, leading to hypothyroidism. Symptoms include fatigue, weight gain, cold intolerance, hair loss, and sometimes thyroid enlargement (goiter). Diagnosis involves thyroid function tests and thyroid antibodies (TPO, thyroglobulin). Treatment is the same as hypothyroidism - thyroid hormone replacement (levothyroxine). Some people may experience periods of hyperthyroid symptoms initially. Regular monitoring is important as hormone needs may change over time. Work with an endocrinologist for optimal management."
                }
            ]
        },
        {
            "name": "Graves' Disease",
            "variations": [
                {
                    "group": "Women (20-50)",
                    "prompts": [
                        "I have hyperthyroid symptoms with bulging eyes.",
                        "What is Graves' disease?",
                        "I have rapid heartbeat, weight loss, and eye problems.",
                        "I feel anxious and my eyes look prominent.",
                        "I have overactive thyroid with eye changes."
                    ],
                    "completion": "Hyperthyroid symptoms (rapid heartbeat, weight loss, anxiety) combined with eye changes (bulging, double vision, eye irritation) suggest Graves' disease, an autoimmune condition causing thyroid overactivity. Eye problems (Graves' ophthalmopathy) may require separate treatment from thyroid specialists and ophthalmologists. Treatment options include antithyroid medications, radioactive iodine, or surgery. Eye symptoms may persist even after thyroid treatment. This condition requires specialized care from an endocrinologist and possibly an ophthalmologist for comprehensive management."
                }
            ]
        },
        
        # PAIN CONDITIONS (Additional)
        {
            "name": "Chronic Fatigue Syndrome",
            "variations": [
                {
                    "group": "Adults (25-55)",
                    "prompts": [
                        "I'm exhausted all the time despite getting enough sleep.",
                        "What are symptoms of chronic fatigue syndrome?",
                        "I feel tired even after resting and have muscle pain.",
                        "How do you treat chronic fatigue?",
                        "I have unexplained fatigue that's lasted for months.",
                        "I feel like I have the flu constantly but tests are normal.",
                        "I have post-exertional malaise and brain fog."
                    ],
                    "completion": "Persistent, unexplained fatigue lasting more than 6 months, not improved by rest, and accompanied by symptoms like muscle pain, cognitive difficulties ('brain fog'), and post-exertional malaise may suggest chronic fatigue syndrome (CFS/ME). This complex condition requires comprehensive medical evaluation to rule out other causes. Management focuses on pacing activities, gentle graded exercise, sleep hygiene, stress management, and treating associated symptoms. There's no cure, but symptoms can be managed. Consult a healthcare provider familiar with CFS for proper diagnosis and individualized treatment plan."
                }
            ]
        },
        {
            "name": "Complex Regional Pain Syndrome",
            "variations": [
                {
                    "group": "Adults (30-60)",
                    "prompts": [
                        "I have severe burning pain in my hand that started after an injury.",
                        "What is complex regional pain syndrome?",
                        "I have intense pain with skin color changes after trauma.",
                        "My pain is much worse than expected for my injury.",
                        "I have burning pain with swelling and skin temperature changes."
                    ],
                    "completion": "Severe, burning pain that's disproportionate to the original injury, with skin color/temperature changes and swelling, may suggest complex regional pain syndrome (CRPS), a chronic pain condition. This typically develops after trauma, surgery, or fractures. Early recognition and treatment are crucial for better outcomes. Treatment includes physical therapy, nerve blocks, medications for neuropathic pain, and sometimes ketamine infusions. If you have severe, persistent pain after an injury that seems excessive, consult a pain management specialist or neurologist promptly for evaluation."
                }
            ]
        },
        
        # SUBSTANCE ABUSE/ADDICTION
        {
            "name": "Opioid Addiction",
            "variations": [
                {
                    "group": "Adults (20-60)",
                    "prompts": [
                        "I was prescribed pain medication and now can't stop taking it.",
                        "What are signs of opioid addiction?",
                        "I need more and more pain pills to feel normal.",
                        "I'm taking prescription drugs not as prescribed.",
                        "I have withdrawal symptoms when I don't take my pain medication.",
                        "I think I'm addicted to prescription painkillers."
                    ],
                    "completion": "Taking prescription opioids in higher doses or more frequently than prescribed, experiencing withdrawal symptoms, or feeling unable to function without them suggests opioid dependence or addiction. This is a medical condition requiring professional treatment, not a moral failing. Treatment options include medication-assisted treatment (buprenorphine, methadone), counseling, and support groups. Sudden cessation can be dangerous - work with healthcare providers for safe tapering or substitution therapy. If you recognize signs of addiction, contact your doctor, an addiction specialist, or call SAMHSA's helpline for confidential support and treatment referrals."
                }
            ]
        },
        
        # COGNITIVE/NEUROLOGICAL CONDITIONS
        {
            "name": "Dementia (Early Signs)",
            "variations": [
                {
                    "group": "Elderly (65+)",
                    "prompts": [
                        "I'm forgetting things more often and getting confused easily.",
                        "What are early dementia symptoms?",
                        "I have trouble finding words and remembering recent events.",
                        "I'm getting lost in familiar places and having trouble with daily tasks.",
                        "My family says I'm more confused and repeat myself.",
                        "I have memory problems that are affecting my daily life."
                    ],
                    "completion": "Memory problems affecting daily life, confusion, difficulty finding words, and getting lost in familiar places may suggest early dementia. While some memory changes are normal with aging, significant impairment that interferes with independence is not normal. Early evaluation is important to rule out treatable causes (medication effects, depression, thyroid problems) and to plan for the future. Treatment may include medications to slow progression, cognitive exercises, and support for patients and families. Consult your primary care provider or a neurologist for comprehensive evaluation."
                }
            ]
        },
        {
            "name": "Concussion",
            "variations": [
                {
                    "group": "Athletes/Active Adults (15-45)",
                    "prompts": [
                        "I hit my head and now have headache with nausea and dizziness.",
                        "What are concussion symptoms?",
                        "I feel confused and have memory problems after hitting my head.",
                        "I have sensitivity to light and sound after a head injury.",
                        "I was in an accident and now have headaches and trouble concentrating.",
                        "I feel foggy and emotional after bumping my head."
                    ],
                    "completion": "Headache, nausea, dizziness, confusion, and light sensitivity after head trauma suggest concussion, a mild traumatic brain injury. Initial management includes physical and cognitive rest, gradual return to activities as symptoms improve, and avoiding activities that could result in another head injury. Most concussions resolve within 7-10 days. Seek immediate medical attention if you experience worsening headache, repeated vomiting, seizures, confusion, or loss of consciousness. Athletes should not return to sports until cleared by a healthcare provider experienced in concussion management."
                }
            ]
        },
        
        # SMOKING-RELATED CONDITIONS
        {
            "name": "Smoking-Related Health Issues",
            "variations": [
                {
                    "group": "Smokers (25-65)",
                    "prompts": [
                        "I'm a smoker with chronic cough and shortness of breath.",
                        "What health problems does smoking cause?",
                        "I want to quit smoking but am worried about withdrawal.",
                        "I have a persistent cough and smoke a pack a day.",
                        "I'm a smoker and getting winded easily with chest tightness."
                    ],
                    "completion": "Chronic cough and shortness of breath in smokers may indicate early COPD, bronchitis, or other smoking-related lung damage. Smoking increases risk of lung cancer, heart disease, stroke, and numerous other conditions. Quitting smoking is the most important step for improving health. Nicotine replacement therapy, prescription medications (varenicline, bupropion), and counseling support increase quit success rates. Withdrawal symptoms are temporary but professional support helps manage them. Contact your healthcare provider or quitline (1-800-QUIT-NOW) for cessation resources and support."
                }
            ]
        },
        
        # KIDNEY/UROLOGICAL (Additional)
        {
            "name": "Benign Prostatic Hyperplasia (BPH)",
            "variations": [
                {
                    "group": "Men (50+)",
                    "prompts": [
                        "I have trouble starting urination and my stream is weak.",
                        "What are prostate enlargement symptoms?",
                        "I wake up multiple times at night to urinate.",
                        "I feel like I can't empty my bladder completely.",
                        "I have urgent need to urinate but only small amounts come out.",
                        "I dribble after urinating and have a weak stream."
                    ],
                    "completion": "Difficulty starting urination, weak stream, frequent nighttime urination, and feeling of incomplete bladder emptying in men over 50 suggest benign prostatic hyperplasia (enlarged prostate). Initial management includes limiting fluids before bedtime, avoiding caffeine and alcohol, and double voiding. If symptoms significantly impact quality of life or you develop urinary retention, consult a urologist. Treatment options include medications to relax prostate muscles or shrink the gland, and surgical procedures for severe cases."
                }
            ]
        },
        {
            "name": "Interstitial Cystitis",
            "variations": [
                {
                    "group": "Women (30-60)",
                    "prompts": [
                        "I have chronic pelvic pain and frequent urination but no infection.",
                        "What is interstitial cystitis?",
                        "I have bladder pain that gets worse as my bladder fills.",
                        "I urinate frequently but urine tests are always normal.",
                        "I have chronic bladder discomfort and pelvic pressure.",
                        "I have pain during intercourse and chronic bladder symptoms."
                    ],
                    "completion": "Chronic pelvic/bladder pain, frequent urination, and urgency without evidence of infection suggest interstitial cystitis (painful bladder syndrome). This condition predominantly affects women and involves bladder wall inflammation. Treatment includes dietary modifications (avoiding acidic foods, caffeine, alcohol), bladder training, pelvic floor physical therapy, and stress management. Medications may include bladder instillations or oral treatments. This chronic condition requires specialized care from a urologist familiar with interstitial cystitis for optimal management."
                }
            ]
        },
        
        # LIVER CONDITIONS (Additional)
        {
            "name": "Alcohol-Related Liver Disease",
            "variations": [
                {
                    "group": "Adults with Alcohol Use (30-65)",
                    "prompts": [
                        "I drink regularly and have fatigue with right upper abdominal pain.",
                        "What are signs of liver damage from alcohol?",
                        "I have yellow skin and my stomach is swollen.",
                        "I drink daily and have been feeling unwell lately.",
                        "I have nausea, fatigue, and my skin looks yellow."
                    ],
                    "completion": "Fatigue, right upper abdominal pain, and jaundice (yellowing of skin/eyes) in someone with regular alcohol use suggest alcohol-related liver disease. This can progress from fatty liver to cirrhosis if alcohol use continues. The most important treatment is complete alcohol cessation. Nutritional support, treating complications, and regular monitoring are essential. If you have signs of liver disease, seek immediate medical evaluation. Treatment may require hospitalization for severe cases. Support for alcohol cessation includes counseling, support groups (AA), and sometimes medications to reduce cravings."
                }
            ]
        },
        
        # BLOOD/CIRCULATORY CONDITIONS
        {
            "name": "Varicose Veins",
            "variations": [
                {
                    "group": "Women (30-60)",
                    "prompts": [
                        "I have bulging, twisted veins in my legs that ache.",
                        "What causes varicose veins?",
                        "My legs feel heavy and I see purple, rope-like veins.",
                        "How do you treat varicose veins?",
                        "I have leg pain and swelling with visible enlarged veins.",
                        "I have aching legs that feel better when I elevate them."
                    ],
                    "completion": "Bulging, twisted, purple veins with leg aching and heaviness indicate varicose veins, more common in women due to hormonal factors and pregnancy. Conservative treatment includes regular exercise, leg elevation when resting, compression stockings, avoiding prolonged standing/sitting, and maintaining healthy weight. Symptoms often improve with these measures. If veins cause significant pain, skin changes, or cosmetic concerns, consult a vascular surgeon for evaluation of treatment options like sclerotherapy, laser therapy, or surgical procedures."
                }
            ]
        },
        {
            "name": "Raynaud's Phenomenon",
            "variations": [
                {
                    "group": "Women (20-50)",
                    "prompts": [
                        "My fingers turn white and blue in cold weather.",
                        "What is Raynaud's phenomenon?",
                        "My hands become numb and discolored when cold.",
                        "I have circulation problems in my fingers and toes.",
                        "My fingers change colors and become painful in the cold."
                    ],
                    "completion": "Fingers or toes that turn white, then blue, then red in response to cold or stress suggest Raynaud's phenomenon, a condition affecting blood flow to extremities. Primary Raynaud's is usually mild and managed with keeping hands/feet warm, avoiding cold exposure, wearing gloves/warm socks, and stress management. Secondary Raynaud's may be associated with autoimmune diseases. If episodes are severe, cause tissue damage, or are associated with other symptoms like joint pain or rashes, consult a rheumatologist for evaluation of underlying conditions."
                }
            ]
        },
        
        # HORMONE-RELATED CONDITIONS
        {
            "name": "Low Testosterone (Hypogonadism)",
            "variations": [
                {
                    "group": "Men (40-70)",
                    "prompts": [
                        "I have low energy, decreased muscle mass, and reduced libido.",
                        "What are low testosterone symptoms?",
                        "I feel depressed and have erectile dysfunction.",
                        "I'm gaining weight and losing muscle despite exercise.",
                        "I have no interest in sex and feel tired constantly.",
                        "I have mood changes and difficulty concentrating."
                    ],
                    "completion": "Low energy, decreased muscle mass, reduced libido, mood changes, and erectile dysfunction in men may suggest low testosterone (hypogonadism). This can occur naturally with aging or due to medical conditions. Diagnosis requires blood testing of testosterone levels, preferably in the morning. Treatment may include testosterone replacement therapy through gels, injections, or patches, but requires careful monitoring for side effects. Lifestyle modifications like weight loss, exercise, and stress management can also help. Consult an endocrinologist or urologist for proper evaluation and treatment planning."
                }
            ]
        },
        {
            "name": "Premenstrual Syndrome (PMS)",
            "variations": [
                {
                    "group": "Women (15-50)",
                    "prompts": [
                        "I have mood changes, bloating, and breast tenderness before my period.",
                        "What are PMS symptoms?",
                        "I get very emotional and irritable the week before my period.",
                        "How do you treat PMS naturally?",
                        "I have physical and emotional symptoms that cycle with my periods.",
                        "I feel depressed and anxious only before menstruation."
                    ],
                    "completion": "Mood changes, bloating, breast tenderness, and irritability in the week before menstruation suggest premenstrual syndrome (PMS). Management includes regular exercise, balanced diet with reduced caffeine/sugar, adequate sleep, stress management, and calcium/magnesium supplements. Track symptoms to confirm cyclical pattern. Over-the-counter pain relievers help physical symptoms. If symptoms are severe or significantly impact daily life (PMDD), hormonal treatments or antidepressants may be helpful. Consult your gynecologist if PMS significantly affects your quality of life or relationships."
                }
            ]
        },
        
        # INFECTIOUS DISEASES (Additional)
        {
            "name": "Whooping Cough (Pertussis)",
            "variations": [
                {
                    "group": "Children/Adults (All Ages)",
                    "prompts": [
                        "I have a severe cough that sounds like 'whooping' when I breathe in.",
                        "What are whooping cough symptoms?",
                        "I have persistent cough with vomiting after coughing fits.",
                        "I was exposed to someone with pertussis.",
                        "I have a cough that's worse at night with choking episodes."
                    ],
                    "completion": "Severe, persistent cough with characteristic 'whooping' sound during inspiration, especially with vomiting after coughing fits, suggests pertussis (whooping cough). This highly contagious bacterial infection can be serious, particularly in infants. Early treatment with antibiotics (azithromycin) reduces severity and contagiousness. Cough suppressants are generally not helpful. Adults and adolescents need Tdap vaccination for prevention. If exposed to pertussis or have persistent severe cough, especially around infants, seek medical evaluation promptly for testing and treatment."
                }
            ]
        },
        {
            "name": "Scabies",
            "variations": [
                {
                    "group": "Adults/Children (All Ages)",
                    "prompts": [
                        "I have intense itching that's worse at night, especially between my fingers.",
                        "What are scabies symptoms?",
                        "I have a rash with small bumps and severe itching.",
                        "I have itching in skin folds and small burrow-like tracks.",
                        "Multiple family members have developed severe itching.",
                        "I have a very itchy rash that spreads to other people."
                    ],
                    "completion": "Intense itching worse at night, especially between fingers, wrists, and skin folds, with small bumps and burrow-like tracks suggests scabies, a highly contagious mite infestation. This condition spreads through close contact and affects entire households. Treatment requires prescription scabicide cream (permethrin) applied to the entire body, washing all clothing/bedding in hot water, and treating all household members simultaneously. Itching may persist for weeks after successful treatment. If you suspect scabies, see your healthcare provider for proper diagnosis and treatment, and inform close contacts about potential exposure."
                }
            ]
        },
        
        # RARE BUT IMPORTANT CONDITIONS
        {
            "name": "Meningitis",
            "variations": [
                {
                    "group": "All Ages",
                    "prompts": [
                        "I have severe headache, high fever, and neck stiffness.",
                        "What are meningitis symptoms?",
                        "I have headache with fever and can't touch my chin to my chest.",
                        "I have sudden severe headache with nausea and light sensitivity.",
                        "I have fever, headache, and a rash that doesn't fade when pressed."
                    ],
                    "completion": "Severe headache, high fever, and neck stiffness (inability to touch chin to chest) suggest meningitis, a life-threatening infection of brain/spinal cord membranes. This is a medical emergency requiring immediate hospital treatment. Additional symptoms may include nausea, vomiting, light sensitivity, confusion, and sometimes a rash that doesn't fade when pressed. Call 911 or go to emergency room immediately - do not wait. Early antibiotic treatment can be life-saving. Bacterial meningitis can cause death or permanent disability within hours if untreated."
                }
            ]
        },
        {
            "name": "Stroke",
            "variations": [
                {
                    "group": "Adults (45+)",
                    "prompts": [
                        "I suddenly can't speak clearly and my face feels droopy.",
                        "What are stroke symptoms?",
                        "I have sudden weakness on one side of my body.",
                        "I have severe headache with confusion and vision changes.",
                        "I can't move my arm and my speech is slurred.",
                        "I have sudden numbness in my face and arm on one side."
                    ],
                    "completion": "Sudden onset of facial drooping, arm weakness, speech difficulties, or other neurological symptoms suggest stroke, a medical emergency. Remember FAST: Face drooping, Arm weakness, Speech difficulties, Time to call 911. Other symptoms include sudden severe headache, vision changes, dizziness, or confusion. Call 911 immediately - do not drive to hospital. Time is critical in stroke treatment ('time is brain'). Emergency treatments can restore blood flow and minimize brain damage if given within hours of symptom onset."
                }
            ]
        },
        
        # SEXUALLY TRANSMITTED INFECTIONS
        {
            "name": "Sexually Transmitted Infections",
            "variations": [
                {
                    "group": "Sexually Active Adults (18-45)",
                    "prompts": [
                        "I have burning during urination and unusual discharge.",
                        "What are STD symptoms?",
                        "I have genital sores and pain during intercourse.",
                        "I have pelvic pain and abnormal bleeding between periods.",
                        "I was exposed to an STI and am worried about symptoms.",
                        "I have itching and unusual vaginal discharge.",
                        "I have pain and discharge from my penis."
                    ],
                    "completion": "Burning urination, unusual discharge, genital sores, or pelvic pain in sexually active individuals may indicate sexually transmitted infections (STIs). Common STIs include chlamydia, gonorrhea, herpes, syphilis, and HPV. Many STIs can be asymptomatic, making regular testing important. Treatment varies by infection but many are curable with antibiotics. Use barrier protection during sexual activity and communicate with partners about STI status. If you have symptoms or potential exposure, see your healthcare provider or visit an STI clinic for confidential testing and treatment."
                }
            ]
        },
        
        # SKIN CONDITIONS (Additional)
        {
            "name": "Fungal Skin Infections",
            "variations": [
                {
                    "group": "Adults/Children (All Ages)",
                    "prompts": [
                        "I have a red, circular rash that's spreading outward.",
                        "What are ringworm symptoms?",
                        "I have itchy, scaling patches on my skin.",
                        "I have athlete's foot with itching between my toes.",
                        "I have a fungal infection in my groin area.",
                        "I have scaling, itchy skin that's worse in warm, moist areas."
                    ],
                    "completion": "Circular, red, scaling rashes that spread outward with central clearing suggest fungal skin infections (ringworm, athlete's foot, jock itch). These are contagious and spread through direct contact or contaminated surfaces. Treatment includes topical antifungal creams (clotrimazole, terbinafine) applied beyond the rash border for 2-4 weeks. Keep affected areas clean and dry, avoid sharing personal items, and wear breathable clothing. If infection is widespread, doesn't improve with topical treatment, or affects nails/scalp, consult your healthcare provider for oral antifungal medications."
                }
            ]
        },
        {
            "name": "Seborrheic Dermatitis",
            "variations": [
                {
                    "group": "Adults (20-60)",
                    "prompts": [
                        "I have flaky, itchy patches on my scalp and face.",
                        "What causes dandruff and facial scaling?",
                        "I have red, greasy patches around my nose and eyebrows.",
                        "How do you treat seborrheic dermatitis?",
                        "I have persistent dandruff and itchy, red patches on my face.",
                        "I have scaling on my scalp that's worse when I'm stressed."
                    ],
                    "completion": "Flaky, itchy, red patches on the scalp, face (especially around nose, eyebrows), and other oily areas suggest seborrheic dermatitis. This common condition is related to yeast overgrowth and oil production. Treatment includes antifungal shampoos (ketoconazole, selenium sulfide), gentle skincare with fragrance-free products, and topical antifungal creams for facial areas. Stress management helps as stress can worsen symptoms. Most cases respond well to over-the-counter treatments. If severe or doesn't improve, consult a dermatologist for prescription treatments."
                }
            ]
        },
        {
            "name": "Hidradenitis Suppurativa",
            "variations": [
                {
                    "group": "Adults (20-50)",
                    "prompts": [
                        "I have painful bumps in my armpits that keep coming back.",
                        "What are recurring boils in skin folds?",
                        "I have deep, painful lumps in my groin area.",
                        "I have chronic abscesses under my arms that drain.",
                        "I have painful nodules in areas where skin rubs together."
                    ],
                    "completion": "Recurring painful bumps, abscesses, or nodules in areas where skin rubs together (armpits, groin, under breasts) suggest hidradenitis suppurativa, a chronic inflammatory skin condition. This condition involves blocked hair follicles and can cause scarring and tunneling under the skin. Treatment includes antibiotics for active infections, anti-inflammatory medications, weight management, and avoiding tight clothing. Severe cases may require biologic medications or surgery. This condition significantly impacts quality of life and requires specialized dermatological care for optimal management."
                }
            ]
        },
        
        # SLEEP DISORDERS (Additional)
        {
            "name": "Sleepwalking",
            "variations": [
                {
                    "group": "Children/Teenagers (5-18)",
                    "prompts": [
                        "My child gets up and walks around while still asleep.",
                        "What is sleepwalking and is it dangerous?",
                        "My teenager does complex activities while sleeping.",
                        "How do you handle sleepwalking episodes?",
                        "My child talks and moves around but doesn't remember it."
                    ],
                    "completion": "Walking, talking, or performing activities while asleep with no memory of the event suggests sleepwalking, most common in children and teenagers. Most children outgrow sleepwalking, but safety is the primary concern. Ensure a safe environment: remove obstacles, secure windows/doors, and consider door alarms. Don't wake sleepwalkers abruptly - gently guide them back to bed. Maintain consistent sleep schedule and manage stress, as these can trigger episodes. If sleepwalking is frequent, dangerous, or persists into adulthood, consult a sleep specialist for evaluation."
                }
            ]
        },
        
        # REPRODUCTIVE HEALTH (Additional)
        {
            "name": "Endometriosis",
            "variations": [
                {
                    "group": "Women (20-40)",
                    "prompts": [
                        "I have severe menstrual pain that's getting worse over time.",
                        "What are endometriosis symptoms?",
                        "I have pelvic pain that's not just during my period.",
                        "I have painful intercourse and heavy periods.",
                        "I have chronic pelvic pain and trouble getting pregnant.",
                        "I have back pain and leg pain during menstruation."
                    ],
                    "completion": "Severe, worsening menstrual pain, chronic pelvic pain outside of periods, painful intercourse, and fertility problems suggest endometriosis, where uterine tissue grows outside the uterus. Pain may radiate to back and legs during menstruation. Treatment includes hormonal therapies to suppress menstruation, pain management, and sometimes surgery. Early diagnosis and treatment can preserve fertility and improve quality of life. If menstrual pain significantly impacts daily activities or you have chronic pelvic pain, consult a gynecologist for evaluation and management."
                }
            ]
        },
        {
            "name": "Fibroids",
            "variations": [
                {
                    "group": "Women (30-50)",
                    "prompts": [
                        "I have very heavy periods and pelvic pressure.",
                        "What are uterine fibroid symptoms?",
                        "I have prolonged menstrual bleeding and abdominal fullness.",
                        "I feel like I have a mass in my pelvis.",
                        "I have frequent urination and heavy menstrual flow.",
                        "I have back pain and pressure in my lower abdomen."
                    ],
                    "completion": "Heavy menstrual bleeding, pelvic pressure, abdominal fullness, and frequent urination suggest uterine fibroids, benign muscle tumors in the uterus. Symptoms depend on size and location of fibroids. Treatment options range from observation for small, asymptomatic fibroids to medications that reduce bleeding or shrink fibroids, and surgical procedures for severe cases. Iron supplementation may be needed for anemia from heavy bleeding. If symptoms significantly impact quality of life, consult a gynecologist for evaluation and treatment options."
                }
            ]
        },
        
        # BONE/JOINT CONDITIONS (Additional)
        {
            "name": "Bursitis",
            "variations": [
                {
                    "group": "Adults (30-60)",
                    "prompts": [
                        "I have pain and swelling over my shoulder/elbow/hip joint.",
                        "What is bursitis?",
                        "I have joint pain that's worse with movement and pressure.",
                        "I have swelling and tenderness over a bony prominence.",
                        "I have shoulder pain that's worse when I lie on it."
                    ],
                    "completion": "Pain, swelling, and tenderness over joints (commonly shoulder, elbow, hip, knee) suggest bursitis, inflammation of fluid-filled sacs that cushion joints. This often results from repetitive activities, direct trauma, or prolonged pressure. Treatment includes rest from aggravating activities, ice application, anti-inflammatory medications, and gentle range-of-motion exercises. Avoid activities that caused the problem until pain subsides. Most cases resolve with conservative treatment in 1-2 weeks. If pain is severe, doesn't improve, or you develop fever, consult your healthcare provider for evaluation and possible injection treatment."
                }
            ]
        },
        {
            "name": "Tendinitis",
            "variations": [
                {
                    "group": "Athletes/Active Adults (25-55)",
                    "prompts": [
                        "I have pain and stiffness in my Achilles tendon after running.",
                        "What are tendinitis symptoms?",
                        "I have shoulder pain that's worse with overhead activities.",
                        "I have wrist pain from repetitive activities.",
                        "I have heel pain and stiffness in my Achilles tendon.",
                        "I have elbow pain from tennis/golf."
                    ],
                    "completion": "Pain, stiffness, and tenderness along tendons (commonly Achilles, rotator cuff, elbow) that worsens with activity suggests tendinitis, inflammation of tendons from overuse or repetitive stress. Treatment includes rest from aggravating activities, ice after activity, anti-inflammatory medications, and gentle stretching. Gradually return to activities as pain improves and modify technique or equipment if needed. Physical therapy can help with proper strengthening and movement patterns. If pain persists despite rest or significantly limits function, consult an orthopedist or sports medicine specialist."
                }
            ]
        },
        
        # ALLERGY CONDITIONS (Additional)
        {
            "name": "Food Allergies",
            "variations": [
                {
                    "group": "Children/Adults (All Ages)",
                    "prompts": [
                        "I have hives, swelling, and stomach upset after eating certain foods.",
                        "What are food allergy symptoms?",
                        "I have immediate reactions when I eat nuts/shellfish.",
                        "I have trouble breathing and swelling after eating.",
                        "I get severe stomach pain and diarrhea after eating specific foods.",
                        "I had a severe allergic reaction and need to avoid certain foods."
                    ],
                    "completion": "Hives, swelling (especially face/throat), stomach upset, or breathing difficulties after eating specific foods suggest food allergies. Common triggers include nuts, shellfish, eggs, milk, soy, and wheat. Mild reactions may involve stomach upset or hives, while severe reactions (anaphylaxis) can be life-threatening with breathing difficulties and shock. Strict avoidance of trigger foods is essential. Carry epinephrine auto-injectors if prescribed. If you suspect food allergies, consult an allergist for testing and management. For severe reactions, seek emergency care immediately."
                }
            ]
        },
        {
            "name": "Eczema (Contact Dermatitis)",
            "variations": [
                {
                    "group": "Adults (All Ages)",
                    "prompts": [
                        "I have red, itchy rash where my skin touched something.",
                        "What is contact dermatitis?",
                        "I have blistering rash after using new soap/cosmetics.",
                        "I have skin reaction after touching plants or chemicals.",
                        "I have localized rash that appeared after exposure to something.",
                        "I have allergic reaction on my skin from jewelry or clothing."
                    ],
                    "completion": "Red, itchy, sometimes blistering rash in areas that contacted an irritant or allergen suggests contact dermatitis. Common triggers include soaps, cosmetics, jewelry (nickel), plants (poison ivy), and chemicals. Treatment involves identifying and avoiding the trigger, washing affected area thoroughly, applying cool compresses, and using topical corticosteroids for inflammation. Oral antihistamines may help itching. If reaction is severe, widespread, or doesn't improve within a week, consult a dermatologist for evaluation and possible allergy testing."
                }
            ]
        },
        
        # VITAMIN DEFICIENCIES (Additional)
        {
            "name": "Vitamin C Deficiency (Scurvy)",
            "variations": [
                {
                    "group": "Adults with Poor Diet (25-65)",
                    "prompts": [
                        "I have bleeding gums and bruise easily.",
                        "What are vitamin C deficiency symptoms?",
                        "I have joint pain and my wounds heal slowly.",
                        "I have fatigue and my teeth feel loose.",
                        "I don't eat fruits or vegetables and have health problems."
                    ],
                    "completion": "Bleeding gums, easy bruising, slow wound healing, and joint pain with inadequate fruit/vegetable intake suggest vitamin C deficiency (scurvy). While rare in developed countries, it can occur with severely restricted diets, alcoholism, or certain medical conditions. Treatment involves vitamin C supplementation and increasing intake of citrus fruits, berries, bell peppers, and leafy greens. Most symptoms improve within days to weeks of adequate vitamin C intake. If you have severe symptoms or underlying conditions affecting nutrition, consult your healthcare provider for proper evaluation and treatment."
                }
            ]
        },
        
        # CIRCULATION/VASCULAR CONDITIONS
        {
            "name": "Peripheral Artery Disease (PAD)",
            "variations": [
                {
                    "group": "Adults (50-80)",
                    "prompts": [
                        "I have leg pain when walking that improves with rest.",
                        "What is peripheral artery disease?",
                        "My legs cramp when I walk and feel better when I stop.",
                        "I have poor circulation in my legs.",
                        "My feet are cold and pale with weak pulses.",
                        "I have claudication pain in my calves when walking."
                    ],
                    "completion": "Leg pain or cramping that occurs with walking and improves with rest (claudication) suggests peripheral artery disease (PAD), reduced blood flow to legs due to arterial blockages. This condition increases risk of heart attack and stroke. Management includes smoking cessation, regular walking exercise, managing diabetes and cholesterol, and blood pressure control. Medications may improve blood flow and reduce clot risk. If symptoms limit mobility or you have non-healing wounds on feet, consult a vascular specialist for evaluation and treatment options."
                }
            ]
        },
        
        # CANCER SYMPTOMS (Early Detection)
        {
            "name": "Colorectal Cancer (Early Signs)",
            "variations": [
                {
                    "group": "Adults (45-75)",
                    "prompts": [
                        "I have changes in bowel habits and blood in my stool.",
                        "What are colon cancer warning signs?",
                        "I have persistent abdominal pain and feel like my bowel doesn't empty completely.",
                        "I have unexplained weight loss and changes in stool consistency.",
                        "I have iron deficiency anemia and digestive symptoms.",
                        "I have family history of colon cancer and new digestive symptoms."
                    ],
                    "completion": "Changes in bowel habits, blood in stool, persistent abdominal pain, feeling of incomplete evacuation, or unexplained weight loss may indicate colorectal cancer, especially in adults over 45 or those with family history. These symptoms warrant prompt medical evaluation with colonoscopy. Many early-stage colorectal cancers are highly treatable when detected early. Follow screening guidelines starting at age 45 (or earlier with family history). If you have concerning symptoms or are due for screening, consult your primary care provider or gastroenterologist for evaluation."
                }
            ]
        },
        {
            "name": "Prostate Cancer (Early Detection)",
            "variations": [
                {
                    "group": "Men (50-75)",
                    "prompts": [
                        "I have urinary problems and my PSA is elevated.",
                        "What are prostate cancer symptoms?",
                        "I have difficulty urinating and pelvic discomfort.",
                        "I have blood in my urine and urinary frequency.",
                        "I have family history of prostate cancer and urinary symptoms."
                    ],
                    "completion": "Urinary difficulties, elevated PSA, blood in urine, or pelvic discomfort in men over 50 may indicate prostate cancer, though many prostate cancers cause no early symptoms. Most urinary symptoms are more commonly due to benign prostate enlargement. Regular screening with PSA testing and digital rectal exam helps detect cancer early when most treatable. Discuss screening benefits and risks with your primary care provider, especially if you have family history or are African American (higher risk). If symptoms are concerning, consult a urologist for evaluation."
                }
            ]
        },
        
        # METABOLIC CONDITIONS
        {
            "name": "Metabolic Syndrome",
            "variations": [
                {
                    "group": "Adults (35-65)",
                    "prompts": [
                        "I have high blood pressure, diabetes, and am overweight around my waist.",
                        "What is metabolic syndrome?",
                        "I have multiple risk factors for heart disease.",
                        "I have insulin resistance and high cholesterol.",
                        "I have abdominal obesity and high triglycerides."
                    ],
                    "completion": "The combination of abdominal obesity, high blood pressure, high blood sugar, and abnormal cholesterol levels constitutes metabolic syndrome, significantly increasing cardiovascular disease and diabetes risk. Management focuses on lifestyle modifications: weight loss (especially abdominal fat), regular exercise, heart-healthy diet (Mediterranean-style), and smoking cessation. Individual components may require medications. The syndrome is reversible with aggressive lifestyle changes. Work with your healthcare provider to address each component and develop a comprehensive plan to reduce cardiovascular risk."
                }
            ]
        },
        
        # AUTOIMMUNE CONDITIONS (Additional)
        {
            "name": "Sjögren's Syndrome",
            "variations": [
                {
                    "group": "Women (40-60)",
                    "prompts": [
                        "I have very dry eyes and dry mouth constantly.",
                        "What causes severe dry eyes and mouth?",
                        "I have joint pain with extreme dryness of eyes and mouth.",
                        "I need to drink water constantly and use eye drops frequently.",
                        "I have autoimmune symptoms with dryness issues."
                    ],
                    "completion": "Severe dry eyes and dry mouth, especially with joint pain or other autoimmune symptoms, suggest Sjögren's syndrome, an autoimmune condition affecting moisture-producing glands. This condition predominantly affects women and can occur alone or with other autoimmune diseases. Treatment includes artificial tears, saliva substitutes, medications to stimulate secretions, and managing associated symptoms. Good oral hygiene is crucial to prevent dental problems. If you have persistent, severe dryness affecting daily life, consult a rheumatologist for evaluation and specialized treatment."
                }
            ]
        },
        
        # SUBSTANCE WITHDRAWAL
        {
            "name": "Caffeine Withdrawal",
            "variations": [
                {
                    "group": "Adults (20-65)",
                    "prompts": [
                        "I stopped drinking coffee and have severe headaches.",
                        "What are caffeine withdrawal symptoms?",
                        "I quit caffeine and feel tired and irritable.",
                        "I have headache and fatigue since stopping coffee.",
                        "I reduced my caffeine intake and feel terrible."
                    ],
                    "completion": "Headaches, fatigue, irritability, and difficulty concentrating after stopping or reducing caffeine suggest caffeine withdrawal. Symptoms typically begin 12-24 hours after last caffeine intake and peak at 1-2 days. Gradual reduction rather than sudden cessation minimizes withdrawal symptoms. Management includes adequate hydration, rest, and over-the-counter pain relievers for headaches. Symptoms usually resolve within a week. If you want to reduce caffeine, decrease intake gradually over several days to weeks to minimize withdrawal effects."
                }
            ]
        },
        
        # AGING-RELATED CONDITIONS
        {
            "name": "Presbyopia",
            "variations": [
                {
                    "group": "Adults (40-65)",
                    "prompts": [
                        "I have trouble reading small print and need to hold things farther away.",
                        "What is presbyopia?",
                        "I need reading glasses and my near vision is blurry.",
                        "I have eye strain when doing close work.",
                        "I can see far away fine but can't focus on close objects."
                    ],
                    "completion": "Difficulty focusing on close objects, needing to hold reading material farther away, and eye strain with near work suggest presbyopia, age-related changes in the eye's focusing ability. This natural aging process typically begins in the 40s. Treatment includes reading glasses, bifocals, progressive lenses, or contact lenses designed for presbyopia. Some people benefit from surgical options. Regular eye exams help monitor changes and ensure proper correction. If you experience sudden vision changes or eye pain, seek immediate eye care evaluation."
                }
            ]
        },
        
        # HORMONAL CONDITIONS (Additional)
        {
            "name": "Insulin Resistance",
            "variations": [
                {
                    "group": "Adults (30-60)",
                    "prompts": [
                        "I have difficulty losing weight and crave sweets constantly.",
                        "What are insulin resistance symptoms?",
                        "I have dark patches on my skin and abdominal weight gain.",
                        "I feel tired after eating and have sugar cravings.",
                        "I have PCOS and difficulty with weight management.",
                        "I have family history of diabetes and weight gain around my middle."
                    ],
                    "completion": "Difficulty losing weight, especially around the waist, constant sugar cravings, fatigue after eating, and dark skin patches (acanthosis nigricans) suggest insulin resistance, a precursor to type 2 diabetes. Management includes low-glycemic diet, regular exercise, weight loss, and sometimes medications like metformin. Focus on whole foods, limit processed carbohydrates, and include protein with meals to stabilize blood sugar. Regular monitoring with glucose and insulin tests helps track improvement. If you have multiple symptoms or risk factors, consult your healthcare provider for evaluation and diabetes prevention strategies."
                }
            ]
        }
 
        # --- Add more diseases and their variations here ---

    ]

    # Convert the structured data into a prompt/completion DataFrame
    processed_data = []
    for disease in common_diseases_data:
        for variation in disease["variations"]:
            for prompt in variation["prompts"]:
                processed_data.append({"prompt": prompt, "completion": variation["completion"]})
            
    df = pd.DataFrame(processed_data)
    
    # Save the dataset
    output_path = '../data/common_diseases_dataset.csv'
    df.to_csv(output_path, index=False)
    
    print(f"Successfully created custom dataset with {len(df)} examples.")
    print(f"Saved to: {output_path}")

if __name__ == '__main__':
    create_common_disease_dataset()
