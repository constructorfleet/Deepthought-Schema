import { loadSchema } from '@graphql-tools/load';
import { makeExecutableSchema } from '@graphql-tools/schema';
import { constraintDirective } from 'graphql-constraint-directive';
import { join } from 'path';
import { GraphQLSchema } from 'graphql';
import { GraphQLFileLoader } from '@graphql-tools/graphql-file-loader';

export const loadGraphQLSchema = async (
  schemaDirectory: string,
): Promise<GraphQLSchema> => loadSchema(
  join(
    schemaDirectory,
    '**',
    '*.graphql',
  ),
  {
    loaders: [
      new GraphQLFileLoader(),
    ],

  },
);

export const applyConstraintDirectivesToSchema = async (
  schema: GraphQLSchema,
): Promise<GraphQLSchema> => constraintDirective()(
  makeExecutableSchema(
    {
      typeDefs: schema,
    },
  ),
);
