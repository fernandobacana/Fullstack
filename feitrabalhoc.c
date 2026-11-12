#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

char nome[100] = "Investidor";
char cpf[12] = "";
char senha[7] = "";
double reais = 0;
double moedas[3] = {0, 0, 0};
double cotacao[3] = {350000, 15000, 2.50};
char nomes[3][20] = {"Bitcoin", "Ethereum", "Ripple"};
char siglas[3][5] = {"BTC", "ETH", "XRP"};
double taxaCompra[3] = {0.02, 0.01, 0.01};
double taxaVenda[3] = {0.03, 0.02, 0.01};

void nomeArquivo(char *destino, char *tipo) {
    sprintf(destino, "%s_%s.txt", tipo, cpf);
}

void salvar() {
    char caminho[60];
    FILE *arquivo;
    nomeArquivo(caminho, "carteira");
    arquivo = fopen(caminho, "w");
    if (arquivo == NULL) { printf("Erro ao salvar carteira.\n"); return; }
    fprintf(arquivo, "%.10f %.10f %.10f %.10f\n", reais, moedas[0], moedas[1], moedas[2]);
    fprintf(arquivo, "%.10f %.10f %.10f\n", cotacao[0], cotacao[1], cotacao[2]);
    fclose(arquivo); 
}

void carregar() {
    char caminho[60];
    FILE *arquivo;
    nomeArquivo(caminho, "carteira");
    arquivo = fopen(caminho, "r");
    reais = 0;
    moedas[0] = moedas[1] = moedas[2] = 0;
    cotacao[0] = 350000; cotacao[1] = 15000; cotacao[2] = 2.50;
    if (arquivo == NULL) { salvar(); return; }
    if (fscanf(arquivo, "%lf %lf %lf %lf", &reais, &moedas[0], &moedas[1], &moedas[2]) != 4 ||
        fscanf(arquivo, "%lf %lf %lf", &cotacao[0], &cotacao[1], &cotacao[2]) != 3) {
        printf("Erro ao ler carteira.\n"); fclose(arquivo); exit(1);
    }
    fclose(arquivo);
}

int somenteNumeros(char *texto, int tamanho) {
    int i;
    if ((int)strlen(texto) != tamanho) return 0;
    for (i = 0; i < tamanho; i++) if (texto[i] < '0' || texto[i] > '9') return 0;
    return 1;
}
int buscarUsuario(char *procurado, char *nomeAchado, char *senhaAchada) {
    FILE *arquivo = fopen("usuarios.txt", "r");
    char n[100], c[30], s[30];
    if (arquivo == NULL) return 0;
    while (fscanf(arquivo, "%99[^;];%29[^;];%29s", n, c, s) == 3) {
        if (strcmp(c, procurado) == 0) {
            strcpy(nomeAchado, n);
            strcpy(senhaAchada, s);
            fclose(arquivo);
            return 1;
        }
    }
    fclose(arquivo);
    return 0;
}
void cadastrar() {
    char novoNome[100], novoCpf[30], novaSenha[30], n[100], s[30];
    FILE *arquivo;
    printf("Nome (sem ponto e virgula): ");
    scanf(" %99[^\n]", novoNome);
    if (strchr(novoNome, ';') != NULL) { printf("Nome invalido.\n"); return; }
    printf("CPF (11 numeros): "); scanf("%29s", novoCpf);
    printf("Senha (6 numeros): "); scanf("%29s", novaSenha);
    if (!somenteNumeros(novoCpf, 11) || !somenteNumeros(novaSenha, 6)) {
        printf("CPF ou senha INVALIDOS.\n"); return;
    }
    if (buscarUsuario(novoCpf, n, s)) { printf("CPF JA POSSUI CADASTRO .\n"); return; }
    arquivo = fopen("usuarios.txt", "a");
    if (arquivo == NULL) { printf("Erro ao abrir usuarios.txt.\n"); return; }
    fprintf(arquivo, "%s;%s;%s\n", novoNome, novoCpf, novaSenha);
    fclose(arquivo);
    printf("Cadastro realizado! Agora faca login.\n");
}

int fazerLogin() {
    char digitado[30], senhaDigitada[30], nomeEncontrado[100], senhaEncontrada[30];
    int tentativas;
    for (tentativas = 0; tentativas < 3; tentativas++) {
        printf("CPF: "); scanf("%29s", digitado);
        printf("Senha: "); scanf("%29s", senhaDigitada);
        if (buscarUsuario(digitado, nomeEncontrado, senhaEncontrada) &&
            strcmp(senhaDigitada, senhaEncontrada) == 0) {
            strcpy(nome, nomeEncontrado);
            strcpy(cpf, digitado);
            strcpy(senha, senhaEncontrada);
            carregar();
            printf("Bem-vindo %s!vamos investir?", nome);
            return 1;
        }
        printf("CPF ou senha incorretos.\n");
    }
    return 0;
}

int confirmarSenha() {
    char digitada[30];
    printf("Digite sua senha: ");
    scanf("%29s", digitada);
    if (strcmp(digitada, senha) != 0) {
        printf("Senha incorreta.\n");
        return 0;
    }
    return 1;
}

void mostrarSaldo() {
    int i;
    printf("\nNome: %s\nCPF: %s\n", nome, cpf);
    printf("Reais: R$ %.2f\n", reais);
    for (i = 0; i < 3; i++) {
        printf("%s: %.8f\n", nomes[i], moedas[i]);
    }
}

void registrar(char operacao, double valor, char *moeda, double preco, double taxa) {
    char caminho[60];
    FILE *arquivo;
    nomeArquivo(caminho, "extrato");
    arquivo = fopen(caminho, "a");
    time_t agora = time(NULL);
    struct tm *data = localtime(&agora);
    if (arquivo == NULL) {
        printf("Nao foi possivel registrar o extrato.\n");
        return;
    }
    fprintf(arquivo, "%02d-%02d-%04d %02d:%02d %c %.2f %s CT: %.2f TX: %.2f REAL: %.2f BTC: %.8f ETH: %.8f XRP: %.8f\n",
        data->tm_mday, data->tm_mon + 1, data->tm_year + 1900,
        data->tm_hour, data->tm_min, operacao, valor, moeda, preco, taxa,
        reais, moedas[0], moedas[1], moedas[2]);
    fclose(arquivo);
}

void extrato() {
    FILE *arquivo;
    char linha[300];
    if (!confirmarSenha()) return;
    { char caminho[60]; nomeArquivo(caminho, "extrato"); arquivo = fopen(caminho, "r"); }
    printf("\nNome: %s\nCPF: %s\n\n", nome, cpf);
    if (arquivo == NULL) {
        printf("Nenhuma operacao realizada.\n");
        return;
    }
    while (fgets(linha, sizeof(linha), arquivo) != NULL) {
        printf("%s", linha);
    }
    fclose(arquivo);
}

void depositar() {
    double valor;
    printf("Valor do deposito: R$ ");
    if (scanf("%lf", &valor) != 1) return;
    if (valor <= 0) {
        printf("Valor invalido.\n");
        return;
    }
    reais += valor;
    salvar();
    registrar('+', valor, "REAL", 0, 0);
    printf("Deposito realizado.\n");
    mostrarSaldo();
}

void sacar() {
    double valor;
    printf("Valor do saque: R$ ");
    if (scanf("%lf", &valor) != 1) return;
    if (valor <= 0 || valor > reais) {
        printf("Valor invalido ou saldo baixo , vamos depositar ?.\n");
        return;
    }
    reais -= valor;
    salvar();
    registrar('-', valor, "REAL", 0, 0);
    printf("Saque feito !.\n");
    mostrarSaldo();
}

void mostrarCotacoes() {
    int i;
    printf("\nCotacoes de hoje:\n");
    for (i = 0; i < 3; i++) {
        printf("%d - %s (%s): R$ %.2f\n", i + 1, nomes[i], siglas[i], cotacao[i]);
    }
}

void negociar(int compra) {
    int escolha, i;
    double valor, taxa, quantidade;
    if (!confirmarSenha()) return;
    mostrarCotacoes();
    printf("Escolha a criptomoeda (1 a 3): ");
    if (scanf("%d", &escolha) != 1) return;
    i = escolha - 1;
    if (i < 0 || i > 2) {
        printf("Moeda invalida, escolha um numero de 1 a 3.\n");
        return;
    }
    if (compra) {
        printf("Quanto deseja gastar ? R$ ");
        if (scanf("%lf", &valor) != 1) return;
        if (valor <= 0 || valor > reais) {
            printf("Valor invalido ou saldo insuficiente.\n");
            return;
        }
        taxa = valor * taxaCompra[i];
        quantidade = (valor - taxa) / cotacao[i];
        reais -= valor;
        moedas[i] += quantidade;
        salvar();
        registrar('+', valor, siglas[i], cotacao[i], taxa);
        printf("Compra realizada: %.8f %s (taxa R$ %.2f).\n", quantidade, siglas[i], taxa);
    } else {
        printf("Quantidade de %s que deseja vender: ", siglas[i]);
        if (scanf("%lf", &quantidade) != 1) return;
        if (quantidade <= 0 || quantidade > moedas[i]) {
            printf("Quantidade invalida ou saldo insuficiente.\n");
            return;
        }
        valor = quantidade * cotacao[i];
        taxa = valor * taxaVenda[i];
        moedas[i] -= quantidade;
        reais += valor - taxa;
        salvar();
        registrar('-', valor, siglas[i], cotacao[i], taxa);
        printf("Venda realizada: R$ %.2f recebidos (taxa de R$ %.2f).\n", valor - taxa, taxa);
    }
    mostrarSaldo();
}

void atualizarCotacoes() {
    int i;
    double variacao;
    for (i = 0; i < 3; i++) {
        variacao = (rand() % 1001 - 500) / 10000.0;
        cotacao[i] = cotacao[i] * (1 + variacao);
    }
    salvar();
    printf("Cotacoes atualizadas.\n");
    mostrarCotacoes();
}

int main() {
    int opcao = 0, entrada;
    srand((unsigned int) time(NULL));
    printf("=== FEICHANGE - CARTEIRA NA PALMA DA MAO ===\n");
    while (1) {
        printf("\n1 - Cadastrar\n2 - Fazer login\n3 - Sair\nOpcao: ");
        if (scanf("%d", &entrada) != 1) return 1;
        if (entrada == 1) cadastrar();
        else if (entrada == 2) { if (fazerLogin()) break; }
        else if (entrada == 3) return 0;
        else printf("Opcao invalida.\n");
    }
    do {
        printf("\n=== MENU ===\n");
        printf("1 - Consultar saldo\n2 - Consultar extrato\n3 - Depositar\n4 - Sacar\n");
        printf("5 - Comprar cripto\n6 - Vender Cripto\n7 - Atualizar cotacao\n8 - Sair\nOpcao: ");
        if (scanf("%d", &opcao) != 1) {
            printf("Entrada invalida.\n");
            return 1;
        }
        switch (opcao) {
            case 1: if (confirmarSenha()) mostrarSaldo(); break;
            case 2: extrato(); break;
            case 3: depositar(); break;
            case 4: sacar(); break;
            case 5: negociar(1); break;
            case 6: negociar(0); break;
            case 7: atualizarCotacoes(); break;
            case 8: printf("Adeus!\n"); break;
            default: printf("Opcao invalida.\n");
        }
    } while (opcao != 8);
    return 0;
}

