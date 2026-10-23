/* Porto Santo Line — comportamento das páginas estáticas de pacotes.
   Replica a interação do site (header, mega-menu, burger, animações por
   data-dentro, FAQ) e o widget de reserva / carrossel dos pacotes. */
(function () {
  'use strict';

  var SITE = 'https://psl-website-web-stage-9bd0ef76c6ce.herokuapp.com';
  var BOOKING = 'https://psl-booking-flow-stage-5ddc0a65b691.herokuapp.com/';
  var S3 = 'https://psl.s3.eu-west-1.amazonaws.com/website/';
  var H = 'Header-module-scss-module__yUQ6Nq__';

  var $ = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };
  var cls = function (name) { return '.' + H + name; };

  /* ---------------------------------------------------------------
     Header: templates do mega-menu (desktop)
     --------------------------------------------------------------- */
  var SETA = '<svg width="13" height="13" viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M3 3l8 8M11 3v8H3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  var SETA_A = SETA.replace('<svg ', '<svg class="' + H + 'botaoSetaA" ');
  var SETA_B = SETA.replace('<svg ', '<svg class="' + H + 'botaoSetaB" ');

  function c(n) { return H + n.split(' ').join(' ' + H); }

  var atraso = 0;
  function cardImagem(href, titulo, desc, img, variante, alt) {
    var a = atraso++;
    return '<a class="' + c('card cardAnima ' + variante) + '" href="' + SITE + href + '" style="--atraso-saida:' + (a * 0.09).toFixed(2) + 's;--atraso-entrada:' + (0.18 + a * 0.14).toFixed(2) + 's">' +
      '<img alt="' + (alt || '') + '" class="' + c('cardImagem') + '" src="' + S3 + img + '" style="position:absolute;height:100%;width:100%;inset:0;object-fit:cover">' +
      '<span class="' + c('cardScrim') + '"></span>' +
      '<span class="' + c('cardConteudo') + '"><span class="' + c('cardTitulo') + '">' + titulo + '</span><span class="' + c('cardDescricao') + '">' + desc + '</span></span>' +
      '<span class="' + c('cardCanto') + '">' + SETA + '</span></a>';
  }
  function cardIcone(href, titulo, desc, icone, variante) {
    var a = atraso++;
    return '<a class="' + c('card cardAnima ' + variante) + '" href="' + SITE + href + '" style="--atraso-saida:' + (a * 0.09).toFixed(2) + 's;--atraso-entrada:' + (0.18 + a * 0.14).toFixed(2) + 's">' +
      '<span class="' + c('cardConteudo') + '"><span class="' + c('cardIcone') + '"><img alt="" src="' + S3 + icone + '" style="position:absolute;height:100%;width:100%;inset:0"></span>' +
      '<span class="' + c('cardTitulo') + '">' + titulo + '</span><span class="' + c('cardDescricao') + '">' + desc + '</span></span>' +
      '<span class="' + c('cardCanto') + '">' + SETA + '</span></a>';
  }
  function menuRodape(href, titulo, desc) {
    return '<a class="' + c('menuRodape') + '" href="' + SITE + href + '"><span class="' + c('menuRodapeTexto') + '">' +
      '<span class="' + c('menuRodapeTitulo') + '">' + titulo + '</span><span class="' + c('menuRodapeDescricao') + '">' + desc + '</span></span>' +
      '<span class="' + c('menuRodapeBotao') + '"><span class="' + c('botaoFill') + '"></span><span class="' + c('botaoRotulo') + '">' +
      '<span class="' + c('botaoRotuloA') + '">Consultar</span><span class="' + c('botaoRotuloB') + '" aria-hidden="true">Consultar</span></span>' +
      '<span class="' + c('botaoSeta') + '">' + SETA_A + SETA_B + '</span></span></a>';
  }
  function interior(html) {
    return '<div class="' + c('painelInterior') + '" data-cards="dentro">' + html + '</div>';
  }

  var PAINEIS = {
    'O Navio': function () {
      atraso = 0;
      return interior('<div class="' + c('cardsLinha') + '">' +
        cardImagem('/o-navio', 'Transporte de Passageiros', 'De lounges confortáveis e restauração a espaços de lazer para toda a família, explore o navio que transforma a sua travessia num momento de puro relaxe.', 'menu_navio_lobo_marinho_f77dbe1ded.jpg', 'cardEstica') +
        '<div class="' + c('coluna') + '"><div class="' + c('cardsLinha') + '">' +
        cardImagem('/transporte-de-viaturas', 'Transporte de Viaturas', 'Acesso ao car deck sem complicações. Descubra como embarcar o seu veículo com total segurança e rapidez.', 'menu_transporte_viaturas_b8c9f6cf0f.jpg', 'cardMedia') +
        cardImagem('/transporte-de-carga', 'Transporte de Carga', 'Assegure o envio de mercadorias com total regularidade e segurança. Consulte tarifas, horários e soluções disponíveis.', 'menu_transporte_carga_60254d0ae9.jpg', 'cardMedia') +
        '</div>' + menuRodape('/regras-e-recomendacoes', 'Regras e Recomendações', 'Tudo o que precisa de saber antes de embarcar. Descubra as regras, recomendações e boas práticas de segurança.') +
        '</div></div>');
    },
    'Explorar as ilhas': function () {
      atraso = 0;
      return interior('<div class="' + c('cardsLinha') + '">' +
        cardImagem('/porto-santo', 'Porto Santo', 'Descubra a ilha dourada: 9 km de praia, miradouros e tranquilidade a apenas uma travessia.', 'menu_porto_santo_b0d91cfe46.jpg', 'cardAlta') +
        cardImagem('/madeira', 'Madeira', 'Explore a ilha da Madeira, das levadas às vilas piscatórias e à gastronomia regional.', 'menu_madeira_3a0192e125.jpg', 'cardAlta') +
        '</div>');
    },
    'Viajar': function () {
      atraso = 0;
      return interior('<div class="' + c('cardsLinha') + '"><div class="' + c('coluna') + '"><div class="' + c('cardsLinha') + '">' +
        cardIcone('/horarios', 'Horários', 'Verifique as partidas diárias disponíveis e organize a sua viagem com total conveniência.', 'icon_horarios_656bf529ba.svg', 'cardMedia cardSolidaClara') +
        cardIcone('/tarifas', 'Tarifas', 'Selecione a sua classe, adicione o seu veículo e descubra as melhores tarifas e pacotes disponíveis.', 'icon_tarifas_7fbcefb036.svg', 'cardMedia cardSolidaEscura') +
        '</div>' + menuRodape('/modos-de-pagamento', 'Modos de pagamento', 'Conheça os métodos de pagamento online e presenciais disponíveis.') + '</div>' +
        '<div class="' + c('card cardAnima cardEstica') + '"><img alt="Família a descer a escada de embarque do navio da Porto Santo Line" class="' + c('cardImagem') + '" src="' + S3 + 'menu_embarque_de076f7f26.jpg" style="position:absolute;height:100%;width:100%;inset:0;object-fit:cover">' +
        '<span class="' + c('cardScrim') + '"></span><span class="' + c('cardConteudo') + '"><span class="' + c('cardTitulo') + '">O Porto Santo está à distância de uma viagem de navio</span>' +
        '<span class="' + c('cardRodape') + '"><span class="' + c('cardDescricao') + '">Reserve já a sua travessia no Lobo Marinho.</span><a class="' + c('cardBotao') + '" href="' + BOOKING + '">Reservar</a></span></span></div>' +
        '</div>');
    },
    'Suporte': function () {
      atraso = 0;
      var itens = [
        ['/faqs', 'Faqs', 'Encontre respostas rápidas para planear a sua viagem sem complicações.'],
        ['/contactos', 'Contactos', 'Estamos prontos para o ajudar antes, durante e após a sua viagem.'],
        ['/subsidio-de-mobilidade', 'Subsídio de Mobilidade', 'Consulte as condições e o processo para solicitar o reembolso do seu subsídio.'],
        ['/contrato-de-passageiros', 'Contrato de Passageiros', 'Aceda aos direitos e deveres associados ao seu bilhete de viagem.'],
        ['/termos-e-condicoes', 'Termos e Condições', 'Conheça as regras e condições de utilização da nossa plataforma online.'],
        ['/protecao-de-dados', 'Proteção de Dados', 'Saiba como recolhemos, utilizamos e protegemos as suas informações pessoais.']
      ];
      return interior('<div class="' + c('grelha') + '">' + itens.map(function (i) {
        return cardIcone(i[0], i[1], i[2], 'icon_pdf_6fdcd779ed.svg', 'cardCompacta');
      }).join('') + '</div>');
    }
  };

  function iniciarHeader() {
    var shell = $(cls('shell'));
    if (!shell) return;
    var header = $(cls('header'), shell);
    var painel = $('#header-megamenu');
    var scrim = $(cls('scrim'));
    var burgerBotao = $(cls('burgerBotao'));
    var burgerPainel = $('#header-burger');
    var pesquisa = $('#header-pesquisa');
    var gatilhos = $$('button' + cls('gatilho'), shell);
    var activo = null;

    function fecharPainel() {
      if (!activo) return;
      activo.setAttribute('aria-expanded', 'false');
      activo = null;
      painel.setAttribute('data-aberto', 'false');
      header.setAttribute('data-painel', 'false');
      scrim.setAttribute('data-aberto', 'false');
    }
    function abrirPainel(btn) {
      var rotulo = $(cls('roloA'), btn);
      var nome = (rotulo || btn).textContent.trim();
      var tpl = PAINEIS[nome];
      if (!tpl) return;
      fecharPesquisa();
      if (activo) activo.setAttribute('aria-expanded', 'false');
      activo = btn;
      painel.innerHTML = tpl();
      btn.setAttribute('aria-expanded', 'true');
      painel.setAttribute('data-aberto', 'true');
      header.setAttribute('data-painel', 'true');
      scrim.setAttribute('data-aberto', 'true');
    }
    gatilhos.forEach(function (btn) {
      if (btn.getAttribute('aria-controls') !== 'header-megamenu') return;
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        if (activo === btn) fecharPainel(); else abrirPainel(btn);
      });
    });

    /* Pesquisa */
    var botaoPesquisa = $('button[aria-controls="header-pesquisa"]');
    function fecharPesquisa() {
      if (!pesquisa) return;
      pesquisa.setAttribute('data-aberta', 'false');
      pesquisa.setAttribute('inert', '');
      if (botaoPesquisa) botaoPesquisa.setAttribute('aria-expanded', 'false');
      scrim.setAttribute('data-pesquisa', 'false');
    }
    if (botaoPesquisa && pesquisa) {
      botaoPesquisa.addEventListener('click', function (e) {
        e.stopPropagation();
        var aberta = pesquisa.getAttribute('data-aberta') === 'true';
        fecharPainel();
        if (aberta) { fecharPesquisa(); return; }
        pesquisa.removeAttribute('inert');
        pesquisa.setAttribute('data-aberta', 'true');
        botaoPesquisa.setAttribute('aria-expanded', 'true');
        scrim.setAttribute('data-pesquisa', 'true');
        var input = $('input', pesquisa);
        if (input) setTimeout(function () { input.focus(); }, 300);
      });
      pesquisa.addEventListener('click', function (e) { e.stopPropagation(); });
    }

    /* Idioma */
    $$(cls('idiomaBotao')).forEach(function (btn) {
      var lista = document.getElementById(btn.getAttribute('aria-controls'));
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        var aberto = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', String(!aberto));
        if (lista) lista.setAttribute('data-aberto', String(!aberto));
      });
    });

    /* Burger (mobile/tablet) */
    if (burgerBotao && burgerPainel) {
      burgerBotao.addEventListener('click', function () {
        var aberto = burgerBotao.getAttribute('aria-expanded') === 'true';
        burgerBotao.setAttribute('aria-expanded', String(!aberto));
        burgerPainel.setAttribute('data-aberto', String(!aberto));
        scrim.setAttribute('data-aberto', String(!aberto));
        document.documentElement.style.overflow = aberto ? '' : 'hidden';
      });
      $$(cls('burgerCabecalho'), burgerPainel).forEach(function (cab) {
        if (cab.tagName !== 'BUTTON') return;
        var corpo = document.getElementById(cab.getAttribute('aria-controls'));
        if (!corpo) return;
        cab.addEventListener('click', function () {
          var aberto = cab.getAttribute('aria-expanded') === 'true';
          cab.setAttribute('aria-expanded', String(!aberto));
          corpo.setAttribute('data-aberto', String(!aberto));
          if (aberto) {
            corpo.style.height = corpo.scrollHeight + 'px';
            requestAnimationFrame(function () { corpo.style.height = '0'; });
            corpo.setAttribute('inert', '');
          } else {
            corpo.removeAttribute('inert');
            corpo.style.height = corpo.scrollHeight + 'px';
            setTimeout(function () { if (cab.getAttribute('aria-expanded') === 'true') corpo.style.height = 'auto'; }, 800);
          }
          burgerPainel.setAttribute('data-seccao', String($$(cls('burgerCabecalho') + '[aria-expanded="true"]', burgerPainel).length > 0));
        });
      });
    }

    function fecharTudo() {
      fecharPainel();
      fecharPesquisa();
      $$(cls('idiomaBotao') + '[aria-expanded="true"]').forEach(function (b) {
        b.setAttribute('aria-expanded', 'false');
        var l = document.getElementById(b.getAttribute('aria-controls'));
        if (l) l.setAttribute('data-aberto', 'false');
      });
    }
    document.addEventListener('click', function (e) {
      if (painel && painel.contains(e.target)) return;
      fecharTudo();
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') fecharTudo(); });
    if (scrim) scrim.addEventListener('click', function () {
      if (burgerBotao && burgerBotao.getAttribute('aria-expanded') === 'true') burgerBotao.click();
      fecharTudo();
    });

    /* Esconder ao fazer scroll para baixo, mostrar ao subir */
    var ultimo = window.scrollY;
    function medir() {
      document.documentElement.style.setProperty('--altura-header', shell.offsetHeight + 'px');
    }
    window.addEventListener('scroll', function () {
      var y = window.scrollY;
      shell.setAttribute('data-no-topo', String(y < 10));
      var aberto = activo || (burgerBotao && burgerBotao.getAttribute('aria-expanded') === 'true');
      var esconder = !aberto && y > 200 && y > ultimo;
      shell.setAttribute('data-escondido', String(esconder));
      document.documentElement.style.setProperty('--header-escondido', esconder ? '1' : '0');
      ultimo = y;
    }, { passive: true });
    window.addEventListener('resize', medir);
    medir();
  }

  /* ---------------------------------------------------------------
     Animações de entrada (data-dentro)
     --------------------------------------------------------------- */
  function iniciarEntradas() {
    var alvos = $$('[data-dentro]');
    if (!('IntersectionObserver' in window)) {
      alvos.forEach(function (el) { el.setAttribute('data-dentro', 'true'); });
      return;
    }
    var io = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.setAttribute('data-dentro', 'true');
          io.unobserve(en.target);
        }
      });
    }, { rootMargin: '0px 0px -5% 0px', threshold: 0 });
    alvos.forEach(function (el) { io.observe(el); });

    /* Reserva: se o observer não disparar, verifica a posição no scroll */
    var pendente = null;
    function verificar() {
      pendente = null;
      var limite = window.innerHeight * 0.95;
      alvos.forEach(function (el) {
        if (el.getAttribute('data-dentro') === 'true') return;
        var r = el.getBoundingClientRect();
        if (r.top < limite && r.bottom > 0) el.setAttribute('data-dentro', 'true');
      });
    }
    function pedir() { if (!pendente) pendente = requestAnimationFrame(verificar); }
    window.addEventListener('scroll', pedir, { passive: true });
    window.addEventListener('resize', pedir);
    window.addEventListener('load', verificar);
    verificar();
  }

  /* ---------------------------------------------------------------
     FAQ (acordeão)
     --------------------------------------------------------------- */
  function iniciarFaq() {
    $$('[class*="Faq-module-scss-module__"][class$="__pergunta"]').forEach(function (btn) {
      var resp = document.getElementById(btn.getAttribute('aria-controls'));
      btn.addEventListener('click', function () {
        var aberta = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', String(!aberta));
        if (resp) resp.setAttribute('data-aberta', String(!aberta));
      });
    });
  }

  /* ---------------------------------------------------------------
     Widget de reserva
     --------------------------------------------------------------- */
  function iniciarReserva() {
    var w = $('.pk-reserva');
    if (!w) return;
    var pax = { adultos: 1, criancas: 0, bebes: 0 };
    var minimos = { adultos: 1, criancas: 0, bebes: 0 };
    var resumo = $$('[data-pax-resumo]', w);
    var partida = $('[name="partida"]', w);
    var regresso = $('[name="regresso"]', w);
    var aviso = $('.pk-reserva__aviso', w);
    var cta = $('.pk-reserva__cta', w);

    function plural(n, s, p) { return n + ' ' + (n === 1 ? s : p); }
    function textoPax() {
      var t = [plural(pax.adultos, 'adulto', 'adultos')];
      if (pax.criancas) t.push(plural(pax.criancas, 'criança', 'crianças'));
      if (pax.bebes) t.push(plural(pax.bebes, 'bebé', 'bebés'));
      return t.join(', ');
    }
    function actualizar() {
      Object.keys(pax).forEach(function (k) {
        var out = $('[data-pax-valor="' + k + '"]', w);
        if (out) out.textContent = pax[k];
        var menos = $('[data-pax="' + k + '"][data-passo="-1"]', w);
        if (menos) menos.disabled = pax[k] <= minimos[k];
      });
      resumo.forEach(function (el) { el.textContent = textoPax(); });
    }
    $$('[data-pax]', w).forEach(function (b) {
      b.addEventListener('click', function () {
        var k = b.getAttribute('data-pax');
        pax[k] = Math.max(minimos[k], Math.min(9, pax[k] + Number(b.getAttribute('data-passo'))));
        actualizar();
      });
    });

    /* Datas: hoje como mínimo; terças-feiras sinalizadas (paragem técnica) */
    var hoje = new Date();
    var iso = function (d) { return d.toISOString().slice(0, 10); };
    if (partida) partida.min = iso(hoje);
    if (regresso) regresso.min = iso(hoje);
    function eTerca(v) { return v && new Date(v + 'T12:00:00').getDay() === 2; }
    function validarDatas() {
      if (partida && regresso && partida.value) {
        regresso.min = partida.value;
        if (regresso.value && regresso.value < partida.value) regresso.value = partida.value;
      }
      var terca = eTerca(partida && partida.value) || eTerca(regresso && regresso.value);
      if (aviso) aviso.hidden = !terca;
    }
    [partida, regresso].forEach(function (i) { if (i) i.addEventListener('change', validarDatas); });

    /* Mobile: barra fixa com expansão do resumo */
    var toggle = $('.pk-reserva__toggle', w);
    if (toggle) {
      toggle.addEventListener('click', function () {
        var aberto = w.getAttribute('data-aberto') === 'true';
        w.setAttribute('data-aberto', String(!aberto));
        toggle.setAttribute('aria-expanded', String(!aberto));
      });
    }

    if (cta) {
      cta.addEventListener('click', function () {
        var q = new URLSearchParams({
          pacote: w.getAttribute('data-pacote') || '',
          origem: 'Funchal', destino: 'Porto Santo',
          partida: partida ? partida.value : '', regresso: regresso ? regresso.value : '',
          adultos: pax.adultos, criancas: pax.criancas, bebes: pax.bebes,
          residente: $('[name="residente"]', w) && $('[name="residente"]', w).checked ? 1 : 0,
          classe: $('[name="primeira"]', w) && $('[name="primeira"]', w).checked ? 'primeira' : 'turistica'
        });
        cta.href = BOOKING + '?' + q.toString();
      });
    }
    actualizar();
  }

  /* ---------------------------------------------------------------
     "Outras Jornadas Ideais" — módulo Journey da home.
     As cards estão repetidas; --k é a posição (card activa = k + 1).
     Ao aproximar-se das pontas, salta n posições sem animação.
     --------------------------------------------------------------- */
  function iniciarJornada() {
    var J = 'Journey-module-scss-module__y-uAEq__';
    $$('[data-jornada]').forEach(function (sec) {
      var n = Number(sec.getAttribute('data-n'));
      var tira = $('.' + J + 'tira', sec);
      var itens = $$('.' + J + 'item', sec);
      var camadas = $$('.' + J + 'camada', sec);
      var total = itens.length;
      var k = 2 * n;
      var passo = 508;

      function medir() {
        if (itens.length > 1) passo = itens[1].offsetLeft - itens[0].offsetLeft || passo;
        tira.style.setProperty('--passo', passo.toFixed(1));
      }
      function aplicar() {
        tira.style.setProperty('--k', k);
        itens.forEach(function (li, i) {
          var visivel = i >= k && i <= k + 2;
          li.setAttribute('aria-hidden', String(!visivel));
          if (visivel) li.removeAttribute('inert'); else li.setAttribute('inert', '');
          var art = $('article', li);
          if (art) art.setAttribute('data-activo', String(i === k + 1));
        });
        camadas.forEach(function (c, i) { c.setAttribute('data-visivel', String(i === (k + 1) % n)); });
      }
      function semAnimacao(fn) {
        sec.setAttribute('data-sem-animacao', 'true');
        fn();
        void tira.offsetWidth;
        sec.setAttribute('data-sem-animacao', 'false');
      }
      function mover(passos) {
        if (!passos) return;
        var destino = k + passos;
        if (destino > total - 3 - n || destino < n) {
          semAnimacao(function () { k += destino > k ? -n : n; aplicar(); });
          destino = k + passos;
        }
        k = Math.max(0, Math.min(total - 3, destino));
        aplicar();
      }

      $('[data-sentido="anterior"]', sec).addEventListener('click', function () { mover(-1); });
      $('[data-sentido="seguinte"]', sec).addEventListener('click', function () { mover(1); });

      /* Arrastar (rato e toque) */
      var inicioX = null, dx = 0, arrastou = false;
      tira.addEventListener('pointerdown', function (e) {
        if (e.button !== 0) return;
        inicioX = e.clientX; dx = 0; arrastou = false;
      });
      window.addEventListener('pointermove', function (e) {
        if (inicioX === null) return;
        dx = e.clientX - inicioX;
        if (!arrastou && Math.abs(dx) > 6) {
          arrastou = true;
          tira.setAttribute('data-arrastando', 'true');
        }
        if (arrastou) tira.style.setProperty('--arrasto', dx.toFixed(1));
      });
      function soltar() {
        if (inicioX === null) return;
        inicioX = null;
        tira.setAttribute('data-arrastando', 'false');
        tira.style.setProperty('--arrasto', '0');
        if (arrastou) mover(Math.round(-dx / passo) || (Math.abs(dx) > 60 ? (dx < 0 ? 1 : -1) : 0));
      }
      window.addEventListener('pointerup', soltar);
      window.addEventListener('pointercancel', soltar);
      tira.addEventListener('click', function (e) {
        if (arrastou) { e.preventDefault(); e.stopPropagation(); arrastou = false; }
      }, true);
      tira.addEventListener('dragstart', function (e) { e.preventDefault(); });

      window.addEventListener('resize', function () { semAnimacao(medir); });
      semAnimacao(function () { medir(); aplicar(); });
    });
  }

  /* ---------------------------------------------------------------
     Indicador de resolução (só para revisão): largura × altura e
     breakpoint do site (768 / 1024 / 1440).
     --------------------------------------------------------------- */
  function iniciarResolucao() {
    var el = $('.pk-resolucao');
    if (!el) return;
    function actualizar() {
      var w = window.innerWidth, h = window.innerHeight;
      var bp = w >= 1440 ? 'Desktop L · ≥1440' : w >= 1024 ? 'Desktop · 1024–1439' : w >= 768 ? 'Tablet · 768–1023' : 'Mobile · <768';
      el.textContent = w + ' × ' + h + ' · ' + bp;
    }
    window.addEventListener('resize', actualizar);
    actualizar();
  }

  /* ---------------------------------------------------------------
     Secção empilhada (desktop): fica presa com o fundo à vista e a
     secção seguinte passa por cima. Se couber no ecrã abaixo do header,
     prende logo abaixo dele; se for mais alta, prende pelo fundo.
     --------------------------------------------------------------- */
  function iniciarEmpilhar() {
    var secs = $$('[data-empilhar]');
    if (!secs.length) return;
    function medir() {
      var header = $(cls('shell'));
      var alturaHeader = header ? header.offsetHeight : 0;
      var desktop = window.innerWidth >= 1024;
      /* Por ordem: a secção que passa por cima tem pelo menos a altura da presa, para a tapar toda */
      secs.forEach(function (s) {
        var seguinte = s.nextElementSibling;
        if (seguinte) seguinte.style.minHeight = '';
        var topo = Math.min(alturaHeader + 15, window.innerHeight - s.offsetHeight - 15);
        s.style.setProperty('--pk-empilhar-topo', Math.round(topo) + 'px');
        /* parte do bloco que fica à vista quando preso (se for mais alto que o ecrã, a de cima sai) */
        var inicioVisivel = Math.max(0, alturaHeader + 15 - topo);
        var visivel = s.offsetHeight - inicioVisivel;
        s.style.setProperty('--pk-empilhar-origem', Math.round(inicioVisivel) + 'px');
        s.style.setProperty('--pk-empilhar-visivel', Math.round(visivel) + 'px');
      });
    }
    window.addEventListener('resize', medir);
    window.addEventListener('load', medir);
    medir();

    /* À medida que a secção seguinte passa por cima, a presa reduz e perde opacidade */
    var pedido = null;
    function animar() {
      pedido = null;
      var desktop = window.innerWidth >= 1024;
      secs.forEach(function (s) {
        var seguinte = s.nextElementSibling;
        if (!desktop || !seguinte) { s.style.transform = ''; s.style.opacity = ''; return; }
        var a = s.getBoundingClientRect(), b = seguinte.getBoundingClientRect();
        var origem = parseFloat(s.style.getPropertyValue('--pk-empilhar-origem')) || 0;
        /* o efeito termina quando a seguinte acaba de subir (altura natural, sem margem extra) */
        var distancia = Math.min(s.offsetHeight - origem, seguinte.offsetHeight) + 15;
        var p = Math.max(0, Math.min(1, 1 - (b.top - (a.top + origem)) / distancia));
        s.style.transform = 'scale(' + (1 - 0.08 * p).toFixed(4) + ')';
        s.style.opacity = (1 - 0.75 * p).toFixed(3);
      });
    }
    function pedir() { if (!pedido) pedido = requestAnimationFrame(animar); }
    window.addEventListener('scroll', pedir, { passive: true });
    window.addEventListener('resize', pedir);
    animar();
  }

  /* ---------------------------------------------------------------
     Teste de cores da card da hero (só para revisão).
     A escolha fica guardada no browser para todas as páginas.
     --------------------------------------------------------------- */
  function iniciarTesteCores() {
    var painel = $('[data-teste-cores]');
    var hero = $('.pk-hero');
    if (!painel || !hero) { if (painel) painel.remove(); return; }
    var grupos = [
      ['veu', 'Véu da imagem', 'site', [
        ['site', 'Atual (site)', 'linear-gradient(#0a142380,#0a142352 45%,#0a142373)'],
        ['reforcado', 'Reforçado', 'linear-gradient(#0a1423a6,#0a142380 45%,#0a1423b3)'],
        ['esquerda', 'Mais escuro à esquerda', 'linear-gradient(90deg,#0a1423d9,#0a142380 45%,#0a142333)'],
        ['base', 'Mais escuro em baixo', 'linear-gradient(#0a142340,#0a142366 40%,#0a1423e0)'],
        ['uniforme', 'Uniforme 60%', '#0a142399']
      ]],
      ['card', 'Cor da card', 'branco', [
        ['amarelo', 'Amarelo', '#f5c842'],
        ['branco', 'Branco', '#ffffff'],
        ['azul-claro', 'Azul-claro', '#d7dde5'],
        ['azul-escuro', 'Azul-escuro', '#153f6a'],
        ['preto', 'Preto', '#141d25']
      ]]
    ];
    painel.innerHTML = grupos.map(function (g) {
      return '<div class="pk-teste-cores__grupo" data-grupo="' + g[0] + '"><span class="pk-teste-cores__titulo">' + g[1] + '</span>' +
        g[3].map(function (o) {
          return '<button type="button" data-opcao="' + o[0] + '" title="' + o[1] + '" aria-label="' + o[1] + '" style="--amostra:' + o[2] + '"></button>';
        }).join('') + '</div>';
    }).join('');
    function aplicar(grupo, opcao) {
      hero.setAttribute('data-teste-' + grupo, opcao);
      $$('[data-grupo="' + grupo + '"] button', painel).forEach(function (b) {
        b.setAttribute('aria-pressed', String(b.getAttribute('data-opcao') === opcao));
      });
      try { localStorage.setItem('pk-teste-' + grupo, opcao); } catch (e) {}
    }
    painel.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-opcao]');
      if (b) aplicar(b.closest('[data-grupo]').getAttribute('data-grupo'), b.getAttribute('data-opcao'));
    });
    grupos.forEach(function (g) {
      var v = g[2];
      try { v = localStorage.getItem('pk-teste-' + g[0]) || g[2]; } catch (e) {}
      aplicar(g[0], v);
    });
  }

  function iniciar() {
    iniciarResolucao();
    iniciarTesteCores();
    iniciarEmpilhar();
    iniciarHeader();
    iniciarEntradas();
    iniciarFaq();
    iniciarReserva();
    iniciarJornada();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar);
  else iniciar();
})();
