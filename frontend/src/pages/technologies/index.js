import { Title, Container, Main } from '../../components'
import styles from './styles.module.css'
import MetaTags from 'react-meta-tags'

const Technologies = () => {
  
  return <Main>
    <MetaTags>
      <title>О проекте</title>
      <meta name="description" content="Фудграм - Технологии" />
      <meta property="og:title" content="О проекте" />
    </MetaTags>
    
    <Container>
    <div className={styles.content}>
        <div>
          <h2 className={styles.subtitle}>Технологии, использованные в проекте</h2>
          <div className={styles.text}>
            <p className={styles.textItem}>
              В разработке Foodgram использован современный стек технологий, позволяющий реализовать полноценный веб-сервис:
            </p>
            <ul className={styles.textItem}>
              <li><strong>Python</strong> — основной язык разработки бэкенда.</li>
              <li><strong>Django</strong> — фреймворк, обеспечивающий быструю и безопасную разработку веб-приложений.</li>
              <li><strong>Django REST Framework</strong> — создание REST API для взаимодействия с фронтендом и внешними сервисами.</li>
              <li><strong>Djoser</strong> — готовое решение для регистрации, авторизации и управления пользователями через API.</li>
              <li><strong>PostgreSQL</strong> — реляционная СУБД для хранения данных.</li>
              <li><strong>Docker</strong> — контейнеризация приложения, упрощающая развёртывание и масштабирование.</li>
              <li><strong>GitHub Actions</strong> — CI/CD: автоматическое тестирование, сборка и деплой после каждого пуша в main.</li>
              <li><strong>Nginx</strong> — веб-сервер и обратный прокси, обеспечивающий стабильную работу фронтенда и API.</li>
            </ul>
            <p className={styles.textItem}>
              Такой подход обеспечивает модульность, масштабируемость и высокую стабильность работы проекта.
            </p>
          </div>
        </div>
      </div>
      
    </Container>
  </Main>
}

export default Technologies

