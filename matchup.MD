```py
# TO DO: combining types 
    # Case: Flying/Steel vs. a Ground type
    #       Ground is strong_against Steel
    #       but since Flying is immune_from Ground
    #       in a matchup you have to handle that.
```
<H2 style="font-family: JetBrains Mono;"> Fire / Water DualType Example </H2>

---
<H3 style="font-family: JetBrains Mono;line-height: 36px;"><i>Raw Output of Combining Before Any Logic:</i></H3>

<blockquote style="line-height:26px;">

${Strong_{against}=\{Grass,Ice,Bug,Steel,Fire,Ground,Rock\}}$

${Weak_{against}=\{Fire,Water(\times 2),Rock,Dragon(\times 2),Grass\}}$

${Resists=\{Fire(\times 2),Grass,Ice(\times 2),Bug,Steel,Fairy,Water,Steel\}}$

${Vulnerable_{to}=\{Water,Ground,Rock,Grass,Electric\}}$

</blockquote>

---

<H3 style="font-family: JetBrains Mono;line-height: 36px;"><i>Logic:</i></H3>

```py
# strong_against <--> weak_against
# if strong_against in weak_against
#       REMOVE both single instances (double will yield one)
```

---

<!-- ${A{out}=\{\}}$ -->

<H3 style="font-family: JetBrains Mono;line-height: 36px;"><i>Processed Output of Combining After Logic:</i></H3>

<blockquote style="line-height:26px;">

${Strong_{against}=\{\begingroup \color{7AC74C} \sout{Grass}\endgroup,Ice,Bug,Steel,\begingroup \color{EE8130}\sout{Fire}\endgroup,Ground,\begingroup \color{B6A136}\sout{Rock}\endgroup\}}$

${Weak_{against}=\{\begingroup \color{EE8130}\sout{Fire}\endgroup,Water(\times 2),\begingroup \color{B6A136}\sout{Rock}\endgroup,Dragon(\times 2),\color{7AC74C}\sout{Grass}\}}$

${Resists=\{Fire(\times 2),\begingroup \color{7AC74C} \sout{Grass}\endgroup,Ice(\times 2),Bug,Steel(\times 2),Fairy,\begingroup \color{6390F0} \sout{Water}\endgroup\}}$

${Vulnerable_{to}=\{\begingroup \color{6390F0} \sout{Water}\endgroup,Ground,Rock,\begingroup \color{7AC74C} \sout{Grass}\endgroup,Electric\}}$

</blockquote>

<H3 style="font-family: JetBrains Mono;line-height: 36px;text-align:center;">↓ ↓ ↓</H3>

<blockquote>

${Strong_{against}=\{Ice,Bug,Steel,Ground\}}$

${Weak_{against}\{Water(\times 2),Dragon(\times 2)\}}$

${Resists=\{Fire(\times 2),Ice(\times 2),Bug,Steel(\times 2),Fairy\}}$

${Vulnerable_{to}=\{Ground,Rock,Electric\}}$

</blockquote>
