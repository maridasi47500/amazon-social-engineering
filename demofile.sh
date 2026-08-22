
mkdir templates 
python3 scaffold.py personne hack_id pic:file nomcomplet prenom nomfamille suffixe titre fm  phone email pays_region_linguistique_id:references description
python3 scaffold.py pays_region_linguistique name
python3 scaffold.py format_de_message personne_id:references texte description
python3 scaffold.py company name  country_region_linguistique_id:references
python3 scaffold.py texte_reseau_sociaux nom_social_media personne_id:references content
python3 scaffold.py texte_reseau_sociaux_company nom_social_media company_id:references content
python3 scaffold.py activities personne_id:references name
python3 scaffold.py human_traits name
python3 scaffold.py hack name
python3 scaffold.py hackhavehumantraits hack_id:references human_traits_id:references
