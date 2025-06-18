from flask import Flask, render_template

app = Flask(__name__)

titulo = "Portal de Eventos Acadêmicos"

from POO import Home
inovasoft = Home()

inovasoft.set_nome("InovaSoft 2025"),
inovasoft.set_nome2("Congresso Acadêmico de Inovação em Engenharia de Software"),
inovasoft.set_data("25 de junho de 2025"),
inovasoft.set_imagem("imagens/inovasoft 2025.png"), 
inovasoft.set_link("inovasoft")

sipengsoft = Home()

sipengsoft.set_nome("SIPEngSoft 2025"),
sipengsoft.set_nome2("Simpósio de Inovação e Práticas em Engenharia de Software"),
sipengsoft.set_data("15 de julho de 2025"),
sipengsoft.set_imagem("imagens/sipengsoft.png"),
sipengsoft.set_link("sipengsoft")

lista_eventos = [inovasoft, sipengsoft]

@app.route("/")
def home():
    return render_template("index.html", eventos=lista_eventos, titulo=titulo)

from POO import Eventos

evento1 = Eventos()

evento1.set_nome("InovaSoft 2025"),
evento1.set_nome2("Congresso Acadêmico de Inovação em Engenharia de Software"),
evento1.set_data("25 de junho de 2025 - 9H as 20H"),
evento1.set_descrição("O InovaSoft 2025 é um evento acadêmico voltado para estudantes, pesquisadores e entusiastas da Engenharia de Software. Durante um dia de programação intensa, o congresso reunirá profissionais renomados, professores universitários e alunos para debaterem os desafios, as tendências e as inovações que estão moldando o futuro do desenvolvimento de software."),
evento1.set_local("Universidade de Vassouras – Campus Principal | Auditório Central"),
evento1.set_palestrante1("Dra. Helena Tavares"),
evento1.set_palestrante2("Prof. Lucas Andrade"),
evento1.set_link1("drahelena"),
evento1.set_link2("proflucas"),
evento1.set_categoria("Tecnologia"),
evento1.set_link3("categorias")

@app.route("/inovasoft")
def inovasoft():
    return render_template("eventos.html", evento = evento1)

evento2 = Eventos()

evento2.set_nome("SIPEngSoft 2025"),
evento2.set_nome2("Simpósio de Inovação e Práticas em Engenharia de Software"),
evento2.set_data("15 de julho de 2025 - 8H as 16H"),
evento2.set_descrição("O Simpósio de Inovação e Práticas em Engenharia de Software (SIPEngSoft 2025) é um evento acadêmico que reúne estudantes, professores e profissionais para discutir as últimas tendências e inovações no desenvolvimento de software. Com o tema Construindo o Futuro com Código, o simpósio abordará temas como Inteligência Artificial, DevOps, metodologias ágeis e testes automatizados, por meio de palestras, workshops e minicursos. Além de compartilhar conhecimentos técnicos, o evento promoverá a interação entre academia e mercado, oferecendo um espaço para startups, empresas e um hackathon. O SIPEngSoft 2025 é uma excelente oportunidade para aprender com especialistas, expandir a rede de contatos e se aprofundar nas práticas que estão moldando o futuro da Engenharia de Software."),
evento2.set_local("Centro de Convenções General Sombra - Universidade de Vassouras"),
evento2.set_palestrante1("Dr. João Pedro Silva"),
evento2.set_palestrante2("Maria Clara Oliveira"),
evento2.set_link1("drjoaopedro"),
evento2.set_link2("mariaclara"),
evento2.set_categoria("Tecnologia"),
evento2.set_link3("categorias")

@app.route("/sipengsoft")
def sipengsoft():
    return render_template("eventos.html", evento = evento2)

from POO import Palestrante

palestrante1 = Palestrante()

palestrante1.set_nome("Dra. Helena Tavares de Carvalho"),
palestrante1.set_imagem("imagens/Dra Helena Tavares.png"),
palestrante1.set_mini_curriculo("Doutora em Engenharia de Software pela Universidade de São Paulo (USP), com mais de 20 anos de experiência no desenvolvimento de soluções digitais centradas no usuário. É referência nacional em UX Engineering e atua como professora titular no Instituto de Tecnologia Aplicada (ITA Digital). Possui publicações reconhecidas internacionalmente nas áreas de interação humano-computador, acessibilidade digital e design emocional. Foi consultora em projetos estratégicos para empresas como Nubank, Embraer e Ministério da Ciência e Tecnologia. Atualmente, lidera o grupo de pesquisa UX Lab Brasil, onde desenvolve metodologias de design empático aplicadas ao ciclo de vida de software. É palestrante recorrente em eventos como QCon, TDC e Latinoware."),
palestrante1.set_evento("InovaSoft 2025"),
palestrante1.set_link("inovasoft")


@app.route("/drahelena")
def drahelena():
    return render_template("palestrante.html", palestrante = palestrante1)

palestrante2 = Palestrante()

palestrante2.set_nome("Prof. Lucas Andrade Pinto"),
palestrante2.set_imagem("imagens/Prof Lucas Andrade.png"),
palestrante2.set_mini_curriculo("Professor na Universidade Federal de Goias, ele é especialista em Arquitetura de Software e defensor de práticas de codificação limpa. Com uma abordagem focada na eficiência e clareza, ele busca ensinar aos seus alunos a importância de escrever códigos sustentáveis e de fácil manutenção. É autor do livro Código Limpo, Mente Limpa, que reflete sua filosofia de trabalho e sua paixão por promover boas práticas de desenvolvimento. Seu objetivo é capacitar futuros profissionais de TI a construir sistemas robustos e bem estruturados, com ênfase na qualidade do código e na ética no desenvolvimento de software."),
palestrante2.set_evento("InovaSoft 2025"),
palestrante2.set_link("inovasoft")


@app.route("/proflucas")
def proflucas():
    return render_template("palestrante.html", palestrante = palestrante2)

palestrante3 = Palestrante()

palestrante3.set_nome("Dr. João Pedro Silva Alencar"),
palestrante3.set_imagem("imagens/Dr João Pedro Silva.png"),
palestrante3.set_mini_curriculo("Dr. João Pedro Silva é Ph.D. em Engenharia de Software pela Universidade de São Paulo (USP) e especialista em Inteligência Artificial aplicada ao desenvolvimento de software. Com mais de 10 anos de experiência na indústria, ele trabalhou em projetos de grande escala em empresas como Google e IBM, além de atuar como consultor para startups inovadoras. Atualmente, é professor e coordenador do Laboratório de IA na USP e autor de diversos artigos sobre a integração de IA no ciclo de vida do software."),
palestrante3.set_evento("SIPEngSoft 2025"),
palestrante3.set_link("sipengsoft"),


@app.route("/drjoaopedro")
def drjoaopedro():
    return render_template("palestrante.html", palestrante = palestrante3)

palestrante4 = Palestrante()

palestrante4.set_nome("Maria Clara Oliveira Valadares"),
palestrante4.set_imagem("imagens/Maria Clara Oliveira.png"),
palestrante4.set_mini_curriculo("Maria Clara Oliveira é especialista em DevOps e metodologias ágeis, com mais de 8 anos de experiência liderando equipes em empresas de tecnologia como Nubank e Dasa. Ela tem um forte foco na implementação de pipelines de integração e entrega contínuas, e na criação de ambientes de desenvolvimento que promovem a colaboração e a eficiência. Maria é também mentora de diversas startups e palestrante em eventos nacionais e internacionais sobre transformação digital e boas práticas de desenvolvimento."),
palestrante4.set_evento("SIPEngSoft 2025"),
palestrante4.set_link("sipengsoft"),


@app.route("/mariaclara")
def mariaclara():
    return render_template("palestrante.html", palestrante = palestrante4)

from POO import Categoria

categoria = Categoria()

categoria.set_nome("Categorias"),
categoria.set_nome2("Veja as categorias abaixo"),
categoria.set_categoria1("Corporativos"),
categoria.set_categoria2("Acadêmicos / Educacionais"),
categoria.set_categoria3("Tecnologia / Inovação"),
categoria.set_categoria4("Culturais"),
categoria.set_categoria5("Esportivos"),
categoria.set_categoria6("Musicais"),
categoria.set_categoria7("Religiosos"),
categoria.set_categoria8("Gastronômicos"),
categoria.set_categoria9("Artes e Exposições"),
categoria.set_categoria10("Feiras e Exposições Comerciais"),
categoria.set_categoria11("Cinema e Teatro"),
categoria.set_categoria12("Beneficentes / Voluntariado"),
categoria.set_categoria13("Infantis"),
categoria.set_categoria14("Casamentos e Festas Sociais"),
categoria.set_categoria15("Moda e Beleza"),
categoria.set_categoria16("Lançamentos de Produtos"),
categoria.set_categoria17("Literários / Clubes de Leitura"),
categoria.set_categoria18("Viagens e Excursões"),
categoria.set_categoria19("Meio Ambiente / Sustentabilidade"),
categoria.set_categoria20("Workshops e Treinamentos")

@app.route("/categorias")
def categorias():
    return render_template("categorias.html", cate = categoria)
