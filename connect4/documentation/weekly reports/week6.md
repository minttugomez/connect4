# Week 6

Hours spent: 4

Korjasin muutaman connect4-luokan funktion ja muutin kolumnien laskennan yksikäsitteisemmäksi. Muutin tekoälyn priorisoimaan keskirivit tasatilanteessa. Tein voiton tarkastus (check_win) -funktion tehokkaammaksi siten, että se tarkastaa vain rivit, joihin viimeisenä laitettu merkki kuuluu. Sama logiikka on lisätty myös AI-luokan voiton testaukseen. Testit päivitetty.

Loin pohjan minimax-algoritmille sillä tasolla, että tekoäly osaa tehdä voiton aiheuttavan siirron, mikäli se on mahdollista. Itse algoritmi, jolle lisään syvyyttä on vielä hieman kesken. Teen sen ensiviikolla ja samoin testit uusille funktioille sekä tekoälylle. Yritän päästä algoritmin kanssa mahdollisimman lähelle tavoitteellista valmista algoritmia ensi viikolla, jotta minulle jää vielä aikaa tehdä yksinkertainen käyttöliittymä sovellukselle ja huolitella muita sovelluksen osa-alueita. Kirjoitan myös dokumentaatiot ensi viikolla.