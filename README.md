# circumbinary-transiting-estimate
This code estimate the tight transit phenomenon in circumbinary system


# Calulating the vertical distance between stars and planets during a transit in a circumbinary system
Since there are two stars in a circumbinary system, we generally consider the transition bewteen the targetd planet and the star you selected.
This will calculate t the minimum vertical distance between a planet and a star in a circumbinary system; by vertical distance we refer to the distance between planet and star in x-y plane (we observe from the z-direction) and notice if there is no inclination for stars and planet, the distance between planet and star in x-y plane would be zero forever.

and this will yield the distance bwteen the star and the planet in the x-y plane with respect to x_b(or the star's coordinate in x axis)
notice, when a transit happen, we could roughly estimate that x_b=x_p (where star's coordinate in x axis  is equal to planet's coordinate in x axis ) and this is where the legitimacy of the code came. and also notice this code use the Approximation of the following of orbital elements (which is true for most of the binary star systems)
* the Argument of periapsis(small omega) for both star and planet is small 
* inclination for both stars and planet are close to  90 deg
* the Longitude of the ascending node(big omega) of the binary star equals zero (you can assign it to be equal to zero by choosing a suitable coordinate)
* the Longitude of the ascending node(big omega) of the planet is small
