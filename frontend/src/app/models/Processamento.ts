export interface Processamento {
  id: number;
  media: number;
  mediana: number;
  status: 'Processando' | 'Concluído';
  criado_em: string;
  numeros: number[];
}
