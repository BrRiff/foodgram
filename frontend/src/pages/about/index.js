import { Title, Container, Main } from '../../components'
import styles from './styles.module.css'
import MetaTags from 'react-meta-tags'

const About = ({ updateOrders, orders }) => {
  
  return <Main>
    <MetaTags>
      <title>О проекте</title>
      <meta name="description" content="Фудграм - О проекте" />
      <meta property="og:title" content="О проекте" />
    </MetaTags>
    
    <Container>
      <div className={styles.content}>
          <div>
            <h2 className={styles.subtitle}>Что такое Foodgram?</h2>
            <div className={styles.text}>
              <p className={styles.textItem}>
                <strong>Foodgram</strong> — это онлайн-платформа для публикации и хранения кулинарных рецептов. Вы можете создавать собственные рецепты, просматривать рецепты других пользователей, добавлять их в избранное и формировать список покупок.
              </p>
              <p className={styles.textItem}>
                Проект разработан в рамках финального спринта обучения на курсе Яндекс Практикума по направлению «Python-разработчик». Он сочетает в себе полный стек современных технологий: Django, PostgreSQL, Docker, GitHub Actions и React.
              </p>
              <p className={styles.textItem}>
                Пользователи могут регистрироваться, подписываться друг на друга, сохранять рецепты, а также быстро получать список необходимых ингредиентов для выбранных блюд.
              </p>
              <p className={styles.textItem}>
                Основная цель — сделать платформу удобной для обмена идеями и планирования покупок. Все просто и понятно, даже если вы заходите сюда впервые.
              </p>
            </div>
          </div>
          <aside>
            <h2 className={styles.additionalTitle}>
              Ссылки
            </h2>
            <div className={styles.text}>
              <p className={styles.textItem}>
                Репозиторий проекта — <a href="#" className={styles.textLink}>GitHub</a>
              </p>
              <p className={styles.textItem}>
                Автор проекта — <a href="#" className={styles.textLink}>Имя Автора</a>
              </p>
            </div>
          </aside>
        </div>

    </Container>
  </Main>
}

export default About

