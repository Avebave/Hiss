man ska kunna välja mellan 10 våningar 
när man väljer en våning kommer den åka antingen uppåt eller neråt och åka åt den riktningen tills ingen mer ska den vägen då kan den byte riktning



Algoritgm beskrivning:
Hissen börjar på fösta våningen, om en knapp trycks på en våning så åker hissen till den våningen
Om hissen åker förbi en våning som har en knapp itryckt med samma riktning som hissen så stannar hissen vid den våningen men åker sen vidare till orginaldestinationen.

Om hissen kommer nerifrån så ska den fortsätta uppåt tills den inte ska mer uppåt, då den vänder och kollar vilka knappar som tryckkts i hissen samt dem som har tryckt neråt knappen på vägen. Man måste kolla med en bool eller loop för att se om en knapp är tryckt och vilket håll den ska.

en bool för alla vånings knappar i hissen, man kollar om någon ovanför/under är true beroende på vilket håll man ska åt