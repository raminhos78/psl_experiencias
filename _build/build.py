#!/usr/bin/env python3
"""Gera as páginas de detalhe dos pacotes "Jornada Ideal" da Porto Santo Line.

Usa a marcação dos componentes das páginas internas do site (Migalha, HeroPage,
InfoCards, MediaChecklist, Locations, Faq e cartões da Journey) com o CSS original
(assets/css/psl.css). Header e footer vêm de _build/partials.

Uso:  python3 _build/build.py
"""
import html
import pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
PARTIALS = pathlib.Path(__file__).resolve().parent / 'partials'
SITE = 'https://psl-website-web-stage-9bd0ef76c6ce.herokuapp.com'
BOOKING = 'https://psl-booking-flow-stage-5ddc0a65b691.herokuapp.com/'
S3 = 'https://psl.s3.eu-west-1.amazonaws.com/website/'

# Prefixos dos módulos CSS do site
M = {
    'migalha': 'Migalha-module-scss-module__6Hh3jW__',
    'hero': 'HeroPage-module-scss-module__fLgBga__',
    'titulo': 'PageTitle-module-scss-module__mhxENq__',
    'info': 'InfoCards-module-scss-module__rsmDgW__',
    'media': 'MediaChecklist-module-scss-module__AJx_Va__',
    'locais': 'Locations-module-scss-module__DsK2fW__',
    'faq': 'Faq-module-scss-module__C6z17W__',
    'jornada': 'Journey-module-scss-module__y-uAEq__',
}


def k(modulo, nomes):
    p = M[modulo]
    return ' '.join(p + n for n in nomes.split())


def e(t):
    return html.escape(t, quote=True)


def separar(texto, modulo, classe='caractere'):
    """Título dividido em palavras/caracteres, como no site (animação de entrada)."""
    i = 0
    palavras = []
    for linha_n, linha in enumerate(texto.split('\n')):
        for p in linha.split():
            chars = ''.join(
                f'<span class="{k(modulo, classe)}" style="--i:{i + n}">{e(ch)}</span>'
                for n, ch in enumerate(p))
            i += len(p)
            palavras.append(f'<span class="{k(modulo, "palavra")}">{chars}</span>')
        if linha_n < texto.count('\n'):
            palavras.append('\n')
    corpo = ' '.join(palavras).replace(' \n ', '\n')
    return (f'<span class="{k(modulo, "nomeAcessivel")}">{e(texto)}</span>'
            f'<span aria-hidden="true">{corpo}</span>')


SETA = ('<svg aria-hidden="true" fill="none" viewBox="0 0 14 14" width="13" height="13">'
        '<path d="M3 3l8 8M11 3v8H3" stroke="currentColor" stroke-linecap="round" '
        'stroke-linejoin="round" stroke-width="1.6"/></svg>')
SETA_NE = ('<svg aria-hidden="true" fill="none" viewBox="0 0 14 14" class="pk-botao__seta">'
           '<path d="M3 3l8 8M11 3v8H3" stroke="currentColor" stroke-linecap="round" '
           'stroke-linejoin="round" stroke-width="1.6"/></svg>')
VISTO = ('<svg aria-hidden="true" class="{cls}" focusable="false" viewBox="0 0 13 9">'
         '<path d="M1 4.5 4.6 8 12 1" fill="none" stroke="currentColor" stroke-linecap="round" '
         'stroke-linejoin="round" stroke-width="1.5"/></svg>')
CRUZ = ('<svg aria-hidden="true" class="{cls}" focusable="false" viewBox="0 0 13 13">'
        '<path d="M2 2l9 9M11 2l-9 9" fill="none" stroke="currentColor" stroke-linecap="round" '
        'stroke-width="1.5"/></svg>')

ICONES = {
    'relogio': '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.6"/><path d="M12 7v5l3 2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    'navio': '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 15l2 5h14l2-5H3zM6 15V9h12v6M9 9V5h6v4" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
    'pino': '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 22s7-6.1 7-11a7 7 0 10-14 0c0 4.9 7 11 7 11z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="12" cy="11" r="2.6" stroke="currentColor" stroke-width="1.6"/></svg>',
    'calendario': '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="3" stroke="currentColor" stroke-width="1.6"/><path d="M3 10h18M8 3v4M16 3v4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    'onda': '<svg aria-hidden="true" data-glifo="alto" fill="none" viewBox="0 0 24 24"><path d="M2 9c2.5 0 2.5-2 5-2s2.5 2 5 2 2.5-2 5-2 2.5 2 5 2M2 15c2.5 0 2.5-2 5-2s2.5 2 5 2 2.5-2 5-2 2.5 2 5 2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    'alerta': '<svg aria-hidden="true" data-glifo="alto" fill="none" viewBox="0 0 24 24"><path d="M12 3l10 18H2L12 3z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M12 10v5M12 18v.01" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    'pessoa': '<svg aria-hidden="true" data-glifo="alto" fill="none" viewBox="0 0 24 24"><circle cx="12" cy="6" r="3" stroke="currentColor" stroke-width="1.6"/><path d="M8 22l1.5-8L8 11h8l-1.5 3L16 22M10 14h4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'carro': '<svg aria-hidden="true" data-glifo="alto" fill="none" viewBox="0 0 24 24"><path d="M4 16v-4l2-5h12l2 5v4H4zM4 16v3M20 16v3M4 12h16" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="8" cy="14" r="1" fill="currentColor"/><circle cx="16" cy="14" r="1" fill="currentColor"/></svg>',
    'raio': '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M13 2L4 14h7l-1 8 9-12h-7l1-8z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
    'apoio': '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 13v-1a8 8 0 0116 0v1" stroke="currentColor" stroke-width="1.6"/><rect x="3" y="13" width="4" height="6" rx="1.5" stroke="currentColor" stroke-width="1.6"/><rect x="17" y="13" width="4" height="6" rx="1.5" stroke="currentColor" stroke-width="1.6"/><path d="M19 19c0 1.5-2 2.5-5 2.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    'troca': '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 8h15l-4-4M20 16H5l4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'aviso': '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true" width="16" height="16" style="flex:none;margin-top:1px"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.6"/><path d="M12 7v6M12 16.5v.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
}
MAIS = '<svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M6 1v10M1 6h10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'
MENOS = '<svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M1 6h10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'
VISTO_CHECK = '<svg viewBox="0 0 9 7" fill="none" aria-hidden="true"><path d="M1 3.4 3.3 5.8 8 1" stroke="#141d25" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# ---------------------------------------------------------------------------
# Conteúdo (psl experiencias.md)
# ---------------------------------------------------------------------------
# Indicador de resolução (largura × altura e breakpoint) para revisão. False = escondido.
INDICADOR_RESOLUCAO = True
# Painel de teste de cores da card da hero (revisão). False = escondido.
TESTE_CORES = False

# Widget de reserva (coluna lateral / barra fixa no mobile). False = escondido.
MOSTRAR_RESERVA = False

PACOTES = [
    {
        'slug': 'viagem-hotel',
        'tag': 'Viagem + Hotel',
        'titulo_card': 'Precisa de desligar e relaxar junto ao mar?',
        'titulo': 'O refúgio perfeito à beira-mar no Hotel Torre Praia',
        'subtitulo': 'Una o conforto da travessia no Lobo Marinho ao descanso de um hotel situado diretamente sobre o areal dourado.',
        'preco': '77,50',
        'img_hero': 'hotel-card.webp', 'pos_hero': 'center center',
        'img_media': 'hotel-media.jpg',
        'alt_hero': 'Quarto do hotel com acesso direto à esplanada e à praia do Porto Santo',
        'alt_media': 'Casal a almoçar numa esplanada com vista para o mar no Porto Santo',
        'factos': ['Mínimo 1 noite (flexível)', 'Estadia Flexível'],
        'destaques': [
            ('Ida e volta', 'Travessia marítima Funchal ↔ Porto Santo (Ida e Volta).'),
            ('Estadia flexível', 'Estadia mínima: 1 noite (flexível).'),
            ('Pequeno-almoço', 'Regime de Pequeno-Almoço buffet incluído.'),
            ('Pés na areia', 'Acesso direto à praia do Torre Praia.'),
        ],
        'inclui': [
            'Bilhete de ferry ida e volta em Lugar Turística ou Primeira Classe.',
            'Noites de alojamento no Hotel Torre Praia em quarto standard com varanda.',
            'Pequeno-almoço buffet diário no restaurante com vista de mar.',
            'Acesso à piscina exterior, sauna, jacuzzi e ginásio do hotel.',
        ],
        'nao_inclui': [
            'Refeições principais (almoços e jantares), salvo seleção de Meia-Pensão.',
            'Transfers locais entre o cais e o hotel (cerca de 5 minutos de táxi).',
        ],
        'faq': [
            ('Posso prolongar a estadia por mais noites?', 'Sim, o widget permite selecionar o intervalo exato de noites pretendido.'),
            ('A que distância fica o hotel da praia?', 'O hotel tem acesso pedonal direto à areia, sem necessidade de atravessar vias rodoviárias.'),
        ],
    },
    {
        'slug': 'viagem-jipe',
        'tag': 'Viagem + Jipe',
        'titulo_card': 'Quer explorar a ilha inteira sem preocupações?',
        'titulo': 'Expedição 4x4: As dunas e o Pico Ana Ferreira em todo-o-terreno',
        'subtitulo': 'Navegue no Lobo Marinho e sinta a natureza do Porto Santo num passeio de jipe 4x4 de 2h30, entre as dunas da ilha e o Pico Ana Ferreira.',
        'preco': '94,40',
        'img_hero': 'jipe-card.webp', 'pos_hero': 'center center',
        'img_media': 'jipe-media.jpg',
        'alt_hero': 'Amigos de braços no ar num jipe entre as dunas do Porto Santo',
        'alt_media': 'Passageiros de braços no ar num jipe aberto durante o tour no Porto Santo',
        'factos': ['Day Trip · passeio de 2h30', 'Dia Completo (Day Trip)'],
        'destaques': [
            ('Passeio de 2h30', 'Duração do passeio todo-o-terreno: 2h30.'),
            ('Jipe 4x4', 'Adrenalina e natureza pelas dunas icónicas da ilha.'),
            ('Pico Ana Ferreira', 'A singularidade do Pico Ana Ferreira.'),
            ('Transferes incluídos', 'Transferes no Funchal ou no Caniço.'),
        ],
        'inclui': [
            'Passagem marítima Funchal ↔ Porto Santo ↔ Funchal no mesmo dia.',
            'Transferes no Funchal ou no Caniço.',
            'Passeio todo-o-terreno de 2h30 em jipe 4x4, pelas dunas e pelo Pico Ana Ferreira.',
        ],
        'nao_inclui': [
            'Refeições e consumos no Porto Santo.',
        ],
        'faq': [
            ('Quanto tempo dura o passeio?', 'Cerca de 2h30, pelas dunas do Porto Santo e pelo Pico Ana Ferreira.'),
            ('Resta tempo para ir à praia?', 'Sim. A saída do Funchal é de manhã e o regresso ao final do dia, por isso fica tempo livre na ilha além do passeio.'),
        ],
    },
    {
        'slug': 'viagem-bicicleta',
        'tag': 'Viagem + Bicicleta',
        'titulo_card': 'Quer pedalar pelos trilhos do Porto Santo?',
        'titulo': 'Porto Santo em Duas Rodas: Liberdade ativa ao longo da costa',
        'subtitulo': 'Viaje no Lobo Marinho e receba uma bicicleta à chegada ao Porto Santo para explorar a ilha ao seu ritmo, com regresso ao final do dia.',
        'preco': '74,10',
        'img_hero': 'bicicleta-card.webp', 'pos_hero': 'center center',
        'img_media': 'bicicleta-media.jpg',
        'alt_hero': 'Ciclistas a pedalar no cais do Porto Santo junto ao mar',
        'alt_media': 'Avenida de palmeiras no Porto Santo com o mar ao fundo',
        'factos': ['Day Trip · bicicleta na ilha', 'Dia Completo (Day Trip)'],
        'destaques': [
            ('Transferes incluídos', 'Transferes no Funchal ou no Caniço.'),
            ('Bicicleta no Porto Santo', 'A bicicleta é entregue à chegada ao Porto Santo.'),
            ('Caução de 25 €', 'Caução devolvida na entrega da bicicleta em boas condições.'),
            ('Dia completo', 'Saída do Funchal de manhã, com regresso ao final do dia.'),
        ],
        'inclui': [
            'Passagem marítima Funchal ↔ Porto Santo ↔ Funchal no mesmo dia.',
            'Transferes no Funchal ou no Caniço.',
            'Bicicleta no Porto Santo, entregue à chegada.',
        ],
        'nao_inclui': [
            'Caução de 25 €, paga na entrega e devolvida com a bicicleta em boas condições.',
        ],
        'faq': [
            ('Onde recebo a bicicleta?', 'À chegada ao Porto Santo, mediante caução de 25 € e apresentação da passagem correspondente ao produto.'),
            ('Quando devolvo a bicicleta?', 'No navio, 50 minutos antes da hora prevista da viagem de regresso ao Funchal. A caução é devolvida se a bicicleta estiver em boas condições (consulte o regulamento).'),
        ],
    },
    {
        'slug': 'viagem-viatura',
        'tag': 'Viagem + Viatura',
        'titulo_card': 'Procura uma pausa no fim de semana?',
        'titulo': 'Leve o seu carro a bordo e percorra a ilha sem restrições',
        'subtitulo': 'Embarque o seu automóvel no porão do Lobo Marinho e usufrua da máxima autonomia com toda a família e bagagem.',
        'preco': '77,50',
        'img_hero': 'viatura-card.webp', 'pos_hero': 'center center',
        'img_media': 'viatura-media.jpg',
        'alt_hero': 'Casal a fotografar-se num miradouro com vista sobre a Vila Baleira',
        'alt_media': 'Vista aérea de um buggy com insufláveis cor-de-rosa no cais do Porto Santo',
        'factos': ['1 dia ou estadia prolongada', 'Day Trip ou Estadia Flexível'],
        'destaques': [
            ('Viatura a bordo', 'Transporte de viatura no convés de carga do ferry.'),
            ('Bagagem sem limite', 'Bagagem no veículo sem limite de peso.'),
            ('Embarque assistido', 'Embarque assistido por oficiais de convés.'),
            ('À sua medida', 'Flexibilidade para passeios de 1 dia ou estadias prolongadas.'),
        ],
        'inclui': [
            'Bilhete de passageiro(s) ida e volta.',
            'Transporte de 1 automóvel ligeiro de passageiros ou carrinha familiar.',
            'Taxas portuárias de movimentação de veículos no Funchal e no Porto Santo.',
        ],
        'nao_inclui': [
            'Combustível e despesas associadas à condução na ilha.',
        ],
        'faq': [
            ('Posso levar malas e cadeiras de praia dentro da viatura?', 'Sim, todo o equipamento acomodado no habitáculo ou porta-bagagens segue sem custos extras.'),
            ('Com que antecedência devo chegar com o carro ao cais?', 'Deve comparecer na rampa de viaturas entre 45 a 60 minutos antes da hora marcada de partida.'),
        ],
    },
    {
        'slug': 'viagem-excursao',
        'tag': 'Viagem + Excursão',
        'titulo_card': 'Deseja conhecer a história e os encantos da ilha?',
        'titulo': 'Volta à Ilha: Os recantos do Porto Santo numa excursão de 2 horas',
        'subtitulo': 'Navegue no Lobo Marinho e percorra o Porto Santo numa excursão de 2 horas, da Calheta ao Pico Castelo e às Serras de Dentro e de Fora.',
        'preco': '89,30',
        'img_hero': 'excursao-hero.jpg', 'pos_hero': 'center 35%',
        'img_media': 'excursao-media.jpg',
        'alt_hero': 'Casal a passear junto à igreja de Nossa Senhora da Piedade, na Vila Baleira',
        'alt_media': 'Casal a visitar o centro histórico da Vila Baleira',
        'factos': ['Day Trip · excursão de 2h', 'Dia Completo (Day Trip)'],
        'destaques': [
            ('Excursão de 2h', 'Duração da excursão: 2 horas.'),
            ('Transferes incluídos', 'Transferes no Funchal ou no Caniço e no Porto Santo.'),
            ('Volta à ilha', 'Da Calheta ao Pico Castelo, Camacha e Portela.'),
            ('Dia completo', 'Saída do Funchal de manhã, com regresso ao final do dia.'),
        ],
        'inclui': [
            'Passagem marítima Funchal ↔ Porto Santo ↔ Funchal no mesmo dia.',
            'Transferes no Funchal ou no Caniço e no Porto Santo.',
            'Excursão de 2 horas com partida do porto do Porto Santo.',
            'Percurso: Calheta, Campo de Cima e Campo de Baixo, Sítio do Dragoal, Pico Castelo, Camacha, Pedregal, Serra de Dentro, Serra de Fora e Portela.',
        ],
        'nao_inclui': [
            'Refeições e consumos no Porto Santo.',
        ],
        'faq': [
            ('Onde começa a excursão?', 'A partida é no porto do Porto Santo, à chegada do Lobo Marinho.'),
            ('Por onde passa a excursão?', 'Calheta, Campo de Cima e Campo de Baixo, Sítio do Dragoal, Pico Castelo, Camacha, Pedregal, Serra de Dentro, Serra de Fora e Portela, em cerca de 2 horas.'),
        ],
    },
    {
        'slug': 'viagem-golfe',
        'tag': 'Viagem + Golfe',
        'titulo_card': 'Quer desafiar os seus limites num campo de classe mundial?',
        'titulo': 'Experiência de Golfe: Um percurso de 18 buracos desenhado por Severiano Ballesteros',
        'subtitulo': 'O clima seco do Porto Santo permite jogar golfe o ano inteiro, num campo de 18 buracos e 6.434 m com vistas sobre as costas Sul e Norte.',
        'preco': '107,10',
        'img_hero': 'golfe-hero.jpg', 'pos_hero': 'center 60%',
        'img_media': 'golfe-media.jpg',
        'alt_hero': 'Golfista com o saco de tacos no campo do Porto Santo Golfe, com a Clubhouse ao fundo',
        'alt_media': 'Golfista a caminhar no relvado do Porto Santo Golfe',
        'factos': ['Day Trip · 18 buracos', 'Dia Completo (Day Trip)'],
        'destaques': [
            ('18 buracos, 6.434 m', 'Campo de 18 buracos e 6.434 m desenhado por Severiano Ballesteros.'),
            ('Green fee incluído', 'Green fee no Campo de Golfe do Porto Santo.'),
            ('Transferes incluídos', 'Transferes no Funchal ou no Caniço e no Porto Santo até ao Clube de Golfe.'),
            ('Vistas panorâmicas', 'Vistas sobre a costa Sul e Norte da ilha.'),
        ],
        'inclui': [
            'Passagem marítima Funchal ↔ Porto Santo ↔ Funchal no mesmo dia.',
            'Green fee no Campo de Golfe do Porto Santo (18 buracos).',
            'Transferes no Funchal ou no Caniço e no Porto Santo até ao Clube de Golfe.',
        ],
        'nao_inclui': [
            'Refeições e consumos no Porto Santo.',
        ],
        'faq': [
            ('Posso jogar golfe em qualquer altura do ano?', 'Sim. O clima seco e com pouca variação de temperatura entre as estações dá ao Porto Santo condições naturais para jogar golfe o ano inteiro.'),
            ('Quem desenhou o campo?', 'O Campo de Golfe do Porto Santo, com 18 buracos e um percurso de 6.434 m, foi desenhado por Severiano Ballesteros.'),
        ],
    },
]

FAQ_COMUM = [
    ('O que acontece se houver avisos meteorológicos?', 'Em caso de avisos meteorológicos da capitania, aplicam-se as políticas de alteração ou cancelamento da viagem.'),
    ('Com que antecedência devo fazer o check-in?', 'Passageiros a pé devem comparecer no terminal 45 minutos antes da partida; passageiros com veículos, 60 minutos antes.'),
]

# Módulo "A experiência a bordo": 'a' = imagem + lista (MediaChecklist), 'b' = estilo Voyage do /o-navio
BORDO_VARIANTE = 'a'

# Dados do Lobo Marinho tal como aparecem no /o-navio (ícones do módulo Voyage)
NAVIO_DADOS = [
    ('voyage_icon_4_f44b7ef4b5.svg', '2h15m', 'Duração da viagem'),
    ('voyage_icon_1_84418f2778.svg', '112m', 'Comprimento'),
    ('voyage_icon_2_dbce558840.svg', '21 nós', 'Velocidade máxima'),
    ('voyage_icon_3_7d867f45b4.svg', '1153', 'Passageiros'),
]

BORDO = [
    'Decks exteriores para contemplação do oceano e observação de cetáceos.',
    'Restaurante self-service, bares e cafetarias com pastelaria fresca.',
    'Cinema a bordo e sala de jogos / espaço infantil.',
    'Acesso Wi-Fi gratuito durante a viagem.',
]

ICONES_DESTAQUES = ['icon_info1_f98d3fbddc.svg', 'icon_info2_4ccb9c20c7.svg',
                    'icon_info3_632d695161.svg', 'icon_info4_d38e11c3b3.svg']


# ---------------------------------------------------------------------------
# Componentes
# ---------------------------------------------------------------------------
def migalha(passos):
    itens = []
    for i, (nome, href) in enumerate(passos):
        ultimo = i == len(passos) - 1
        conteudo = e(nome) if ultimo or not href else f'<a href="{href}">{e(nome)}</a>'
        actual = ' aria-current="page"' if ultimo else ''
        itens.append(f'<li class="{k("migalha", "degrau")}"{actual}>{conteudo}</li>')
    return (f'<nav aria-label="Onde está" class="{k("migalha", "migalha")}">'
            f'<ol class="{k("migalha", "lista")}">{"".join(itens)}</ol></nav>')


def hero(p):
    return f'''<section aria-labelledby="pk-titulo" class="{k('hero', 'hero')} pk-hero" id="section-0">
<div class="{k('hero', 'media')}"><div class="{k('hero', 'mediaGradiente')}"></div>
<img alt="{e(p['alt_hero'])}" class="{k('hero', 'imagem')}" decoding="async" fetchpriority="high" src="assets/img/{p['img_hero']}" style="position:absolute;height:100%;width:100%;left:0;top:0;right:0;bottom:0;color:transparent;object-position:{p['pos_hero']}">
<div class="{k('hero', 'scrim')}"></div></div>
<div class="{k('hero', 'conteudo')}"><div class="{k('hero', 'linha')}"><div>
<div class="pk-hero__topo"><span class="pk-pilula pk-pilula--amarela">{e(p['tag'])}</span></div>
<h1 class="{k('hero', 'titulo')}" id="pk-titulo">{separar(p['titulo'], 'hero')}</h1><p class="{k('hero', 'intro')}">{e(p['subtitulo'])}</p></div>
{cartao_hero(p)}</div></div>
<div class="{k('hero', 'ancora')}"><div class="{k('hero', 'linha')}"><span class="{k('hero', 'pergunta')}">Podemos ajudar?</span><svg aria-hidden="true" class="{k('hero', 'balao')}" fill="none" viewBox="0 0 54 36"><path d="M42 0C48.6274 0 54 5.37258 54 12V24C54 30.6274 48.6274 36 42 36H0V12C0 5.37258 5.37258 0 12 0H42Z" fill="currentColor"/><circle class="{k('hero', 'ponto')}" cx="17.5" cy="18.5" data-ordem="0" r="3.5"/><circle class="{k('hero', 'ponto')}" cx="27.5" cy="18.5" data-ordem="1" r="3.5"/><circle class="{k('hero', 'ponto')}" cx="37.5" cy="18.5" data-ordem="2" r="3.5"/></svg><a class="{k('hero', 'botao')}" href="https://wa.me/351962025500?text={e('Olá, gostaria de informações sobre o pacote ' + p['tag'] + '.')}" rel="noopener noreferrer" target="_blank"><span class="{k('hero', 'nome')}">Falar connosco no WhatsApp</span><svg aria-hidden="true" class="{k('hero', 'glifo')}" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2a10 10 0 00-8.6 15L2 22l5.2-1.4A10 10 0 1012 2zm0 2a8 8 0 016.9 12l-.3.5.6 2.2-2.3-.6-.5.3A8 8 0 1112 4zm-3.4 4c-.2 0-.5 0-.7.4-.3.3-1 1-1 2.4s1 2.8 1.2 3c.2.2 2 3.1 4.9 4.3 2.4 1 2.9.8 3.4.8.5-.1 1.7-.7 1.9-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.6-.3l-2-1c-.3-.1-.5-.2-.7.1l-.7 1c-.2.2-.3.2-.6.1-.3-.2-1.3-.5-2.5-1.6-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.5-.6.3-.5v-.5l-.9-2.1c-.2-.5-.4-.5-.6-.5h-.5z"/></svg></a></div></div>
</section>'''


def cartao_hero(p, classe=''):
    """Card branca com os destaques, o preço e o Reservar. Em tablet e mobile é mostrada a cópia fora da hero."""
    return f'''<div class="pk-hero__lado{classe}">{factos(p, 'pk-factos--card')}<div class="pk-hero__acoes"><p class="pk-hero__preco"><span class="pk-hero__desde">Desde</span><span class="pk-hero__valor">{p['preco']} €</span></p>{botao_jornada('Reservar', BOOKING + '?pacote=' + p['slug'], 'pk-hero__cta')}</div></div>'''


def factos(p, classe=''):
    # Ícones do site (cronómetro do /o-navio, calendário do motor de reservas), a amarelo
    rotulos = [('Duração', 'duracao'), ('Modalidade', 'modalidade')]
    itens = ''.join(
        f'<li class="pk-factos__item" style="--i:{i}"><span class="pk-factos__rotulo"><img class="pk-factos__icone" alt="" src="assets/img/icons/{ic}.svg">{r}</span>'
        f'<p class="pk-factos__valor">{e(v)}</p></li>'
        for i, ((r, ic), v) in enumerate(zip(rotulos, p['factos'])))
    return f'<ul class="pk-factos {classe}" aria-label="Destaques rápidos" data-dentro="false">{itens}</ul>'


def info_cards(antetitulo, titulo, cartoes, sid, empilhar=False):
    itens = ''.join(f'''<li class="{k('info', 'item')}" data-sozinho="false" style="--i:{i}"><div class="{k('info', 'cartao')}" data-estilo="white"><div class="{k('info', 'miolo')}"><div class="{k('info', 'topo')}"><span class="{k('info', 'icone')}"><img alt="" loading="lazy" src="assets/img/icons/check.svg" style="position:absolute;height:100%;width:100%;left:0;top:0;right:0;bottom:0;color:transparent"></span><p class="{k('info', 'cartaoTitulo')}">{e(t)}</p></div><div class="{k('info', 'corpo cartaoTexto')}"><p>{e(d)}</p></div></div></div></li>'''
                    for i, (t, d) in enumerate(cartoes))
    empilhar = ' data-empilhar' if empilhar else ''
    return f'''<section aria-labelledby="{sid}-titulo" class="{k('info', 'seccao')}" data-dentro="false"{empilhar} id="{sid}">
<div class="{k('info', 'cabecalho')}">{f'<p class="{k("info", "antetitulo")}">{e(antetitulo)}</p>' if antetitulo else ''}<h2 class="{k('info', 'titulo')}" id="{sid}-titulo">{separar(titulo, 'info', 'caractereTitulo')}</h2></div>
<ul class="{k('info', 'cartoes')}" style="--cartoes:{len(cartoes)}">{itens}</ul></section>'''


def media_checklist(sid, titulo, intro, img, alt, grupos, invertida=False, nota='', cta=None, empilhar=False):
    gs = []
    for i, (gtitulo, icone, itens, negativo) in enumerate(grupos):
        marca = (CRUZ if negativo else VISTO).format(cls=k('media', 'visto') + (' pk-visto--nao' if negativo else ''))
        lis = ''.join(f'<li class="{k("media", "item")}">{marca}<span class="{k("media", "itemTexto")}">{e(t)}</span></li>' for t in itens)
        gs.append(f'''<li class="{k('media', 'grupo')}" style="--i:{i}"><div class="{k('media', 'grupoCabeca')}"><span class="{k('media', 'pastilha')}"><img alt="" loading="lazy" src="{S3}{icone}" style="position:absolute;height:100%;width:100%;left:0;top:0;right:0;bottom:0;color:transparent"></span><h3 class="{k('media', 'grupoTitulo')}" id="{sid}-g{i}">{e(gtitulo)}</h3></div><ul aria-labelledby="{sid}-g{i}" class="{k('media', 'itens')}">{lis}</ul></li>''')
    extra = ' pk-media--invertida' if invertida else ''
    nota_html = f'<p class="pk-checklist-nota">{e(nota)}</p>' if nota else ''
    cta_html = botao_jornada(cta[0], cta[1], 'pk-checklist-cta') if cta else ''
    empilhar = ' data-empilhar' if empilhar else ''
    return f'''<section aria-labelledby="{sid}-titulo" class="{k('media', 'seccao')}{extra}" data-dentro="false"{empilhar} id="{sid}">
<div class="{k('media', 'grelha')}"><div class="{k('media', 'moldura')}"><img alt="{e(alt)}" class="{k('media', 'fotografia')}" loading="lazy" src="assets/img/{img}" style="position:absolute;height:100%;width:100%;left:0;top:0;right:0;bottom:0;color:transparent;object-fit:cover"></div>
<div class="{k('media', 'coluna')}"><h2 class="{k('media', 'titulo')}" id="{sid}-titulo">{separar(titulo, 'media')}</h2><p class="{k('media', 'intro')}">{e(intro)}</p><ul class="{k('media', 'grupos')}">{''.join(gs)}</ul>{nota_html}{cta_html}</div></div></section>'''


BORDO_ICONES = [
    '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M2 15c2.5 0 2.5-2 5-2s2.5 2 5 2 2.5-2 5-2 2.5 2 5 2M2 20c2.5 0 2.5-2 5-2s2.5 2 5 2 2.5-2 5-2 2.5 2 5 2M7 10V5h10v5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 10h13v4a5 5 0 01-5 5H9a5 5 0 01-5-5v-4zM17 11h1.5a2.5 2.5 0 010 5H16M8 3c0 1.5 1 1.5 1 3M12 3c0 1.5 1 1.5 1 3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="3" y="6" width="18" height="13" rx="2.5" stroke="currentColor" stroke-width="1.6"/><path d="M10 10l5 2.5-5 2.5v-5zM7 3l3 3M17 3l-3 3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M2.5 9a14 14 0 0119 0M5.5 12.5a9.5 9.5 0 0113 0M8.5 16a5 5 0 017 0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="12" cy="19.5" r="1.2" fill="currentColor"/></svg>',
]


def bordo_b(sid):
    """Proposta B: módulo imersivo inspirado no "Voyage" do /o-navio."""
    dados = ''.join(
        f'<li class="pk-bordo__dado" style="--i:{i}"><span class="pk-bordo__icone"><img alt="" loading="lazy" src="{S3}{ic}"></span>'
        f'<span class="pk-bordo__numero">{e(n)}</span><span class="pk-bordo__rotulo">{e(r)}</span></li>'
        for i, (ic, n, r) in enumerate(NAVIO_DADOS))
    comodidades = ''.join(
        f'<li class="pk-bordo__cartao" style="--i:{i}"><span class="pk-bordo__icone pk-bordo__icone--svg">{BORDO_ICONES[i]}</span>'
        f'<p>{e(texto)}</p></li>'
        for i, texto in enumerate(BORDO))
    return f'''<section aria-labelledby="{sid}-titulo" class="pk-bordo" data-dentro="false" id="{sid}">
<div class="pk-bordo__fundo" aria-hidden="true"><img class="pk-bordo__mar" alt="" loading="lazy" src="assets/img/bordo-mar.webp"><img class="pk-bordo__navio" alt="" loading="lazy" src="assets/img/bordo-navio.webp"><span class="pk-bordo__veu"></span></div>
<div class="pk-bordo__conteudo">
<p class="pk-bordo__antetitulo">A bordo do Lobo Marinho</p>
<h2 class="pk-bordo__titulo" id="{sid}-titulo">A viagem também faz parte da experiência</h2>
<p class="pk-bordo__intro">2h15 de travessia com todo o conforto, entre o Funchal e o Porto Santo.</p>
<ul class="pk-bordo__dados" aria-label="O navio em números">{dados}</ul>
<h3 class="pk-bordo__subtitulo">Comodidades a bordo</h3>
<ul class="pk-bordo__cartoes">{comodidades}</ul>
{botao('Conhecer o navio', SITE + '/o-navio', 'pk-botao--branco pk-bordo__cta')}
</div></section>'''


def locais_termos(sid):
    def linha(icone, rotulo, valor):
        return (f'<div class="{k("locais", "linha")}"><span class="{k("locais", "icone")}">{ICONES[icone]}</span>'
                f'<span class="{k("locais", "oculto")}">{e(rotulo)}:</span><p class="{k("locais", "valor")}">{e(valor)}</p></div>')

    def cartao(estilo, nome, linhas, href, accao):
        return (f'<li class="{k("locais", "cartao")}" data-estilo="{estilo}"><div class="{k("locais", "corpo")}"><div class="{k("locais", "texto")}">'
                f'<h3 class="{k("locais", "nome")}">{e(nome)}</h3><div class="{k("locais", "detalhes")}">{"".join(linhas)}</div></div>'
                f'{botao_jornada(accao, SITE + href, "pk-termos-cta")}</div></li>')

    c1 = cartao('solidPaleBlue', 'Condições do mar', [
        linha('onda', 'Política', 'Alteração ou cancelamento da viagem em caso de avisos meteorológicos da capitania.'),
    ], '/regras-e-recomendacoes', 'Regras e recomendações')
    c2 = cartao('solidYellow', 'Check-in no terminal', [
        linha('pessoa', 'Passageiros a pé', 'Passageiros a pé: comparecer 45 min antes da partida.'),
        linha('carro', 'Veículos', 'Passageiros com veículos: comparecer 60 min antes da partida.'),
    ], '/horarios', 'Ver horários')
    return f'''<section aria-labelledby="{sid}-titulo" class="{k('locais', 'seccao')}" data-dentro="false" id="{sid}">
<img alt="" class="{k('locais', 'fotografia')}" loading="lazy" src="assets/img/termos-fundo.jpg" style="position:absolute;height:100%;width:100%;left:0;top:0;right:0;bottom:0;color:transparent;object-fit:cover">
<span aria-hidden="true" class="{k('locais', 'veu')}"></span>
<div class="{k('locais', 'cabecalho')}"><p class="{k('locais', 'antetitulo')}">Termos, condições e segurança marítima</p><h2 class="{k('locais', 'titulo')}" id="{sid}-titulo">Viaje informado
e em total segurança</h2></div>
<ul class="{k('locais', 'cartoes')}">{c1}{c2}</ul></section>'''


def faq(sid, perguntas):
    linhas = []
    for i, (q, r) in enumerate(perguntas):
        aberta = 'true' if i == 0 else 'false'
        linhas.append(f'''<div class="{k('faq', 'linha')}" style="--i:{i}"><h3 class="{k('faq', 'perguntaCabeca')}"><button aria-controls="{sid}-r{i}" aria-expanded="{aberta}" class="{k('faq', 'pergunta')}" id="{sid}-p{i}" type="button"><span aria-hidden="true" class="{k('faq', 'numero')}">{i + 1:02d}</span><span class="{k('faq', 'perguntaTexto')}">{e(q)}</span><span aria-hidden="true" class="{k('faq', 'icone')}"><span class="{k('faq', 'barraDeitada')}"></span><span class="{k('faq', 'barraEmPe')}"></span></span></button></h3><div aria-labelledby="{sid}-p{i}" class="{k('faq', 'resposta')}" data-aberta="{aberta}" id="{sid}-r{i}" role="region"><div class="{k('faq', 'respostaInterior')}"><div class="{k('faq', 'corpo respostaTexto')}"><p>{e(r)}</p></div></div></div></div>''')
    return f'''<section aria-labelledby="{sid}-titulo" class="{k('faq', 'seccao')}" id="{sid}">
<div class="{k('faq', 'cabecalho')}" data-dentro="false"><p class="{k('faq', 'antetitulo')}">Perguntas frequentes</p><h2 class="{k('faq', 'titulo')}" id="{sid}-titulo">{separar('Tudo o que precisa de saber antes de reservar este pacote.', 'faq', 'caractereTitulo')}</h2></div>
<div class="{k('faq', 'lista')}" data-dentro="false">{''.join(linhas)}</div></section>'''


def botao_jornada(texto, href, extra=''):
    """Botão das cards da Jornada do site (texto e seta ↘ que rolam no hover)."""
    return (f'<a class="{k_("botao")} {extra}" href="{href}"><span class="{k_("nomeAcessivel")}">{e(texto)}</span>'
            f'<span aria-hidden="true" class="{k_("enchimento")}"></span><span aria-hidden="true" class="{k_("conteudo")}">'
            f'<span class="{k_("rolo")}"><span class="{k_("roloA")}">{e(texto)}</span><span class="{k_("roloB")}">{e(texto)}</span></span>'
            f'<span class="{k_("rolo")}"><span class="{k_("roloA")}">{SETA}</span><span class="{k_("roloB")}">{SETA}</span></span></span></a>')


def botao(texto, href, extra='', attrs=''):
    return (f'<a class="pk-botao {extra}" href="{href}"{attrs}><span class="pk-botao__enchimento" aria-hidden="true"></span>'
            f'<span class="pk-botao__rolo"><span class="pk-botao__a">{e(texto)}</span><span class="pk-botao__b" aria-hidden="true">{e(texto)}</span></span>{SETA_NE}</a>')


def reserva(p):
    def pax(chave, nome, nota, inicial):
        nota_html = f'<small>{e(nota)}</small>' if nota else ''
        return (f'<li class="pk-pax__linha"><span class="pk-pax__nome">{e(nome)}{nota_html}</span><span class="pk-pax__controlo">'
                f'<button type="button" class="pk-passo" data-pax="{chave}" data-passo="-1" aria-label="Remover {e(nome.lower())}">{MENOS}</button>'
                f'<output class="pk-pax__valor" data-pax-valor="{chave}" aria-live="polite">{inicial}</output>'
                f'<button type="button" class="pk-passo" data-pax="{chave}" data-passo="1" aria-label="Adicionar {e(nome.lower())}">{MAIS}</button></span></li>')

    def check(nome, texto, nota=''):
        nota_html = f'<small>{e(nota)}</small>' if nota else ''
        return (f'<label class="pk-check"><input type="checkbox" name="{nome}"><span class="pk-check__caixa" aria-hidden="true">{VISTO_CHECK}</span>'
                f'<span>{e(texto)}{nota_html}</span></label>')

    preco = f'<p class="pk-reserva__desde">Desde</p><p class="pk-reserva__preco">{p["preco"]} €<small>/pessoa</small></p>'
    return f'''<aside class="pk-reserva" data-aberto="false" data-pacote="{p['slug']}" aria-label="Reservar {e(p['tag'])}">
<div class="pk-reserva__cartao" id="pk-reserva-corpo">
<div class="pk-reserva__cabeca"><div><span class="pk-pilula">{e(p['tag'])}</span></div><div class="pk-reserva__preco-bloco">{preco}</div></div>
<form class="pk-reserva__campos" onsubmit="return false">
<div class="pk-campo"><span class="pk-campo__rotulo">Origem / Destino</span><div class="pk-campo__caixa pk-rota"><span>Funchal</span>{ICONES['troca']}<span>Porto Santo</span></div></div>
<div class="pk-datas">
<label class="pk-campo"><span class="pk-campo__rotulo">Data de partida</span><input type="date" name="partida"></label>
<label class="pk-campo"><span class="pk-campo__rotulo">Data de regresso</span><input type="date" name="regresso"></label>
</div>
<p class="pk-reserva__nota">Calendário sincronizado com a grelha de viagens do Lobo Marinho, incluindo viagens extraordinárias.</p>
<p class="pk-reserva__aviso" hidden>{ICONES['aviso']}<span>Às terças-feiras o Lobo Marinho pode estar em paragem técnica. Confirme a disponibilidade da data escolhida.</span></p>
<fieldset class="pk-campo"><legend class="pk-campo__rotulo" style="margin-bottom:.5rem">Passageiros · <span data-pax-resumo>1 adulto</span></legend>
<ul class="pk-pax">{pax('adultos', 'Adultos', '', 1)}{pax('criancas', 'Crianças', '4–11 anos', 0)}{pax('bebes', 'Bebés', '0–3 anos', 0)}</ul></fieldset>
{check('residente', 'Residente na Região Autónoma da Madeira', 'Aplica a tarifa de residente')}
<fieldset class="pk-campo"><legend class="pk-campo__rotulo" style="margin-bottom:.625rem">Opções de conforto</legend>{check('primeira', 'Upgrade para 1ª Classe Panorâmica')}</fieldset>
</form>
{botao('Reservar Agora', BOOKING, 'pk-reserva__cta')}
<ul class="pk-garantias">
<li><span class="pk-garantias__icone">{ICONES['raio']}</span>Confirmação imediata</li>
<li><span class="pk-garantias__icone">{ICONES['apoio']}</span>Apoio ao Cliente Oficial PSL</li>
</ul>
</div>
<div class="pk-reserva__barra">
<button type="button" class="pk-reserva__toggle" aria-expanded="false" aria-controls="pk-reserva-corpo"><span class="pk-reserva__desde">Desde</span><span class="pk-reserva__preco">{p['preco']} €</span><span class="pk-reserva__toggle-texto">Ver resumo <svg viewBox="0 0 10 6" fill="none" aria-hidden="true"><path d="M1 5l4-4 4 4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span></button>
{botao('Reservar Agora', BOOKING, 'pk-reserva__cta')}
</div>
</aside>'''


def cartao_jornada(p, activo=False):
    return f'''<article class="{k('jornada', 'cartao')}" data-activo="{'true' if activo else 'false'}"><p class="{k('jornada', 'etiqueta')}"><span class="{k('jornada', 'pilula')}">{e(p['tag'])}</span></p><h3 class="{k('jornada', 'tituloCartao')}">{e(p['titulo_card'])}</h3><p class="{k('jornada', 'descricao')}">{e(p['subtitulo'])}</p><div class="{k('jornada', 'moldura')}"><img alt="{e(p['alt_hero'])}" class="{k('jornada', 'imagem')}" loading="lazy" src="assets/img/{p['img_hero']}" style="position:absolute;height:100%;width:100%;left:0;top:0;right:0;bottom:0;color:transparent;object-position:{p['pos_hero']}"></div><div class="{k('jornada', 'rodape')}"><div><p class="{k('jornada', 'desde')}">Desde</p><p class="{k('jornada', 'preco')}">{p['preco']}</p></div><a class="{k('jornada', 'botao')}" href="{p['slug']}.html"><span class="{k('jornada', 'nomeAcessivel')}">Ver pacote — {e(p['titulo_card'])}</span><span aria-hidden="true" class="{k('jornada', 'enchimento')}"></span><span aria-hidden="true" class="{k('jornada', 'conteudo')}"><span class="{k('jornada', 'rolo')}"><span class="{k('jornada', 'roloA')}">Ver pacote</span><span class="{k('jornada', 'roloB')}">Ver pacote</span></span><span class="{k('jornada', 'rolo')}"><span class="{k('jornada', 'roloA')}">{SETA}</span><span class="{k('jornada', 'roloB')}">{SETA}</span></span></span></a></div></article>'''


REPETICOES = 5  # o carrossel da home repete as cards para dar a volta sem fim


def jornadas(actual):
    """Módulo "Journey" da home: cards em arco, card activa a amarelo e fundo da card activa."""
    outros = [p for p in PACOTES if p['slug'] != actual['slug']]
    n = len(outros)
    k = 2 * n  # posição inicial, como na home (--k = 2 × número de cards)
    activo = k + 1
    camadas = ''.join(
        f'<div class="{k_("camada")}" data-visivel="{"true" if i == activo % n else "false"}">'
        f'<img alt="" class="{k_("imagemFundo")}" loading="lazy" src="assets/img/{p["img_hero"]}" '
        f'style="position:absolute;height:100%;width:100%;left:0;top:0;right:0;bottom:0;color:transparent;object-position:{p["pos_hero"]}"></div>'
        for i, p in enumerate(outros))
    itens = []
    for idx in range(n * REPETICOES):
        p = outros[idx % n]
        visivel = k <= idx <= k + 2
        entrada = 0 if idx <= k else (1 if idx == k + 1 else 2)
        attrs = ' aria-hidden="false"' if visivel else ' aria-hidden="true" inert=""'
        itens.append(f'<li class="{k_("item")}" data-entrada="{entrada}"{attrs} style="--indice:{idx}">'
                     f'<div class="{k_("arco")}">{cartao_jornada(p, idx == activo)}</div></li>')
    seta = ('<svg aria-hidden="true" fill="none" height="18" viewBox="0 0 15 18" width="15"><path d="M8.76074 6.19531C9.05365 5.90255 9.52844 5.90246 9.82129 6.19531L14.5938 10.9678C14.8866 11.2607 14.8866 11.7364 14.5938 12.0293L9.82129 16.8018C9.52844 17.0946 9.05365 17.0945 8.76074 16.8018C8.46795 16.5089 8.46795 16.0341 8.76074 15.7412L12.2529 12.25H1.75C1.33581 12.2499 1.00006 11.9142 1 11.5C1 11.0857 1.33578 10.7501 1.75 10.75H12.2529L8.76074 7.25879C8.46795 6.9659 8.46795 6.4912 8.76074 6.19531Z" fill="currentColor"/></svg>')

    def botao_seta(sentido, rotulo):
        return (f'<button aria-label="{rotulo}" class="{k_("seta")}" data-sentido="{sentido}" type="button">'
                f'<span aria-hidden="true" class="{k_("enchimentoSeta")}"></span><span aria-hidden="true" class="{k_("roloSeta")}">'
                f'<span class="{k_("setaA")}">{seta}</span><span class="{k_("setaB")}">{seta}</span></span></button>')

    titulo = 'Inspire-se e escolha a sua\npróxima jornada'
    return f'''<section aria-label="Outras Jornadas Ideais" class="{k_('seccao')} pk-jornada" data-jornada data-n="{n}" data-dentro="false" data-sem-animacao="false">
<div aria-hidden="true" class="{k_('fundo')}">{camadas}<div class="{k_('scrim')}"></div></div>
<h2 class="{k_('titulo')}">{separar(titulo, 'jornada').replace(f'<span aria-hidden="true">', f'<span aria-hidden="true" class="{k_("envolucro")}">', 1)}</h2>
<div class="{k_('tira')}" data-arrastando="false" style="--k:{k}"><ul aria-label="Outras jornadas ideais" class="{k_('pista')}">{''.join(itens)}</ul></div>
<div class="{k_('setas')}">{botao_seta('anterior', 'Pacote anterior')}{botao_seta('seguinte', 'Pacote seguinte')}</div>
</section>'''


def destaques_v2(p):
    """Destaques numerados (vindos da antiga versão 2), título à esquerda."""
    itens = ''.join(
        f'<li class="pk2-dest__item" style="--i:{i}"><span class="pk2-dest__num">{i + 1:02d}</span>'
        f'<h3 class="pk2-dest__titulo">{e(t)}</h3><p class="pk2-dest__texto">{e(d)}</p></li>'
        for i, (t, d) in enumerate(p['destaques']))
    return f'''<section aria-labelledby="section-1-titulo" class="pk2-dest" data-dentro="false" id="section-1">
<div class="pk2-dest__cabeca"><p class="pk2-dest__ante">Porque vai gostar</p><h2 class="pk2-dest__h2" id="section-1-titulo">{e(p['titulo_card'])}</h2></div>
<ol class="pk2-dest__lista">{itens}</ol>
</section>'''


def tabs_experiencias(p):
    """Tabs flutuantes com as 6 experiências."""
    actual = ' aria-current="page"'
    tabs = ''.join(
        f'<a href="{o["slug"]}.html"{actual if o["slug"] == p["slug"] else ""}>'
        f'{e(o["tag"].removeprefix("Viagem + "))}</a>'
        for o in PACOTES)
    return f'<nav class="pk-experiencias" aria-label="Experiências">{tabs}</nav>'


def k_(nomes):
    return k('jornada', nomes)


# ---------------------------------------------------------------------------
# Página
# ---------------------------------------------------------------------------
def pagina(titulo, descricao, corpo, classe_body=''):
    header = (PARTIALS / 'header.html').read_text().replace('{{ROOT}}', '')
    footer = (PARTIALS / 'footer.html').read_text().replace('{{ROOT}}', '')
    return f'''<!doctype html>
<html lang="pt" class="afacad_e4c77ff-module__cB9SYG__variable editorial_26a60d64-module__2cuXFW__variable">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titulo)} | Porto Santo Line</title>
<meta name="description" content="{e(descricao)}">
<link rel="icon" href="{S3}favicon_251029f904.ico" type="image/vnd.microsoft.icon">
<link rel="preload" href="assets/fonts/6b91545418f16b52-s.p.20g0z6qjw1ulq.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/PPEditorialNew_Regular-s.p.103svg8q-rxix.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/psl.css">
<link rel="stylesheet" href="assets/css/pacotes.css">
</head>
<body class="{classe_body}">
<a class="layout-module-scss-module__gOsIXW__skipLink" href="#main">Saltar para o conteúdo principal</a>
{header}
<main aria-label="Conteúdo principal" id="main" tabindex="-1">
{corpo}
<div class="pk-espaco-rodape"></div>
</main>
{footer}
{'<div class="pk-resolucao" aria-hidden="true"></div>' if INDICADOR_RESOLUCAO else ''}
{'<div class="pk-teste-cores" data-teste-cores></div>' if TESTE_CORES else ''}
<script src="assets/js/psl.js" defer></script>
</body>
</html>
'''


def pagina_pacote(p):
    corpo = '\n'.join([
        migalha([('Início', SITE + '/'), ('Pacotes & Experiências', 'index.html'), (p['tag'], None)]),
        hero(p),
        cartao_hero(p, ' pk-hero__lado--fora'),
        '<div class="pk-layout">' if MOSTRAR_RESERVA else '<div class="pk-layout pk-layout--sem-reserva">',
        '<div class="pk-conteudo">',
        '<div class="pk-empilhado">',
        '<div class="pk-empilhado__grupo" data-empilhar>',
        destaques_v2(p),
        media_checklist('section-2', 'O que está incluído', 'Tudo o que precisa para aproveitar o Porto Santo, numa única reserva.',
                        p['img_media'], p['alt_media'],
                        [('Incluído no pacote', 'icon_tickers_f1204dcdf4.svg', p['inclui'], False),
                         ('Não inclui', 'icon_danger_f35a3fb3cc.svg', p['nao_inclui'], True)]),
        '</div>',
        bordo_b('section-3') if BORDO_VARIANTE == 'b' else
        media_checklist('section-3', 'A experiência a bordo do Lobo Marinho',
                        'A viagem também faz parte da experiência: 2h15 de travessia com todo o conforto.',
                        'bordo-media.jpg', 'Casal no convés do Lobo Marinho a olhar para o Porto Santo',
                        [('Comodidades a bordo', 'voyage_icon_1_84418f2778.svg', BORDO, False)], invertida=True,
                        cta=('Conhecer o navio', SITE + '/o-navio')),
        '</div>',
        locais_termos('section-4'),
        faq('section-5', p['faq'] + FAQ_COMUM),
        '</div>',
        reserva(p) if MOSTRAR_RESERVA else '',
        '</div>',
        jornadas(p),
        tabs_experiencias(p),
    ])
    return pagina(p['tag'], p['subtitulo'], corpo, 'pk-tem-reserva' if MOSTRAR_RESERVA else '')


def pagina_indice():
    titulo = 'Pacotes & Experiências'
    cabeca = f'''<section aria-labelledby="section-0-titulo" class="{k('titulo', 'seccao')}" id="section-0"><h1 class="{k('titulo', 'titulo')}" id="section-0-titulo">{separar(titulo, 'titulo')}</h1><p class="{k('titulo', 'intro')}">Inspire-se e escolha
a sua jornada ideal</p></section>'''
    cartoes = ''.join(f'<li>{cartao_jornada(p)}</li>' for p in PACOTES)
    corpo = '\n'.join([
        migalha([('Início', SITE + '/'), (titulo, None)]),
        cabeca,
        f'<ul class="pk-grelha">{cartoes}</ul>',
    ])
    return pagina(titulo, 'Combine a viagem no Lobo Marinho com hotel, jipe, bicicleta, viatura, excursão ou golfe no Porto Santo.', corpo)


def main():
    (RAIZ / 'index.html').write_text(pagina_indice())
    for p in PACOTES:
        (RAIZ / f"{p['slug']}.html").write_text(pagina_pacote(p))
    print('Geradas:', 'index.html', *[p['slug'] + '.html' for p in PACOTES])


if __name__ == '__main__':
    main()
