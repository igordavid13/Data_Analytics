## 🔥 Introdução

A [VLGI]() é um grupo empresarial composto por diversas empresas do setor financeiro. Entre elas estão:
A [VLGI Investimentos](https://vlginvestimentos.com.br/), empresa credenciada à [XP](https://www.xpi.com.br/) e que atua na assessoria de investimentos.
A [VLGI School](https://school.vlgi.com.br/), focada no ensino sobre investimentos. 
A [VLGI Vida](https://vlgivida.com.br/), especializada em soluções para planejamento financeiro. A [VLGI Corporate](https://vlgicorporate.com.br/), focada em soluções financeiras personalizadas para pessoas físicas e jurídicas.
E a [VLGI Asset]() gestora de investimentos do grupo.

Todas essas estruturas têm a necessidade comum de possuir dados bem estruturados, confiáveis e disponíveis para consulta.
Como `Analistas de Dados`, precisamos criar estruturas capazes de satisfazer a essas necessidades e usar essas informações para o aprimoramento dos nossos produtos e processos a fim de auxiliar na tomada de decisões na empresa.

## 🧩 Sobre o Desafio

A VLGI Asset é uma gestora de carteira administrada, ela provém um serviço que, simplificadamente, funciona da seguinte maneira:

Ao se tornar cliente, a pessoa abre uma conta e concorda com uma política de investimentos.
Essa política define os percentuais de alocação para classes de ativos que devem ser cumpridas.
A política do cliente é baseada no [perfil suitability](https://comoinvestir.anbima.com.br/noticia/suitability-entenda-perfil-investidor/),
que é uma categoria que indica os investimentos adequados para um cliente.
O cliente então faz o aporte de um valor em dinheiro.
A partir desse ponto, a VLGI Asset fará a gestão desse valor 
alocando em uma carteira de investimentos que esteja de acordo com a política do cliente e realocando quando necessário.
A carteira de investimentos é o conjunto de ativos nos quais o cliente possui algum valor alocado.

Periodicamente, o time operacional da VLGI Asset precisa realocar os ativos nas contas dos clientes. Para fazer isso, eles priorizam as contas menos aderentes à política, uma vez que estas possuem a posição atual mais distantes da sua política de investimentos. __Seu objetivo é ajudar o time operacional informando quais são as contas que devem ser priorizadas__.

Nesse contexto, a pasta `data` contém dois conjuntos de dados. O primeiro, `fake_position.csv`,
possui dados fictícios das __posições__ das contas dos clientes. As posições se referem aos valores alocados em cada ativo na carteira do cliente.
O segundo, `fake_allocation_policies.xlsx`, possui a __política__ de investimentos e a relação dos percentuais desejados das carteiras por perfil suitability. As posições se relacionam com as políticas por meio do perfil suitability.
Os dados são fictícios e foram gerados usando a biblioteca [faker](https://github.com/joke2k/faker). Apesar disso, a sua estrutura se assemelha bastante à estrutura real dos dados.

O seu desafio será composto das seguintes etapas:

1. Instanciar um banco de dados __PostgreSQL__ e realizar nele a ingestão dos dados. Isso pode ser feito localmente da forma que preferir, apenas indique o passo a passo adotado.

1. Criar uma consulta SQL que retorne a aderência das contas à sua política de investimentos.

    Dica: Uma possível métrica para calcular a aderência é a [Distância Euclidiana](https://pt.wikipedia.org/wiki/Dist%C3%A2ncia_euclidiana).

1. Criar um dashboard para disponibilizar as informações de aderência para o time operacional. Você pode usar o Python ou a plataforma de visualização que preferir, apenas adicione a imagem do dashboard na documentação do seu projeto.

    Bônus: Disponibilizar outras informações que você julgar relevantes para o time operacional.

## 🎯 Como avaliamos

Avaliamos todos os aspectos do desafio e cada etapa concluída, então, não se preocupe apenas com o resultado.
Para lhe guiar, seguem alguns aspectos que consideramos:

- Processo de desenvolvimento da solução;
- Processamentos de dados realizados;
- Resultados alcançados;
- Uso do git para o versionamento do código do projeto;
- Criação de código limpo;
- Documentação do código e do projeto.

## 📦 Como fazer a entrega
- O projeto deve ser entregue como um repositório público no **Gitlab** ou **Github**. Nele não deve haver qualquer indicação ou uso da marca VLGI.
- O repositório deve conter instruções completas para executarmos a solução em nossas próprias máquinas.
- Você terá 7 dias corridos completos para trabalhar no projeto, a contar da data posterior ao envio do desafio.
- Avaliaremos a sua solução em até 7 dias corridos para lhe dar o resultado.
- Caso tenha alguma dúvida quanto a proposta do desafio, por favor, entre em contato conosco.