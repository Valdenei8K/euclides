FROM node:20 as build

WORKDIR /app

COPY . .

RUN npm install
RUN npm run build

FROM nginx:alpine


COPY --from=build /app/dist/challenge/browser /usr/share/nginx/html


COPY nginx/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
