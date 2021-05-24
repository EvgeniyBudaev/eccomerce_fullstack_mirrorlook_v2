import React from 'react'
import { Route, Switch } from 'react-router-dom'
import MainLayout from "../Layouts/MainLayout"
import {ROUTES} from '../../routes'
import AboutPage from '../About'

export const App = () => {
    return (
        <MainLayout>
            <Switch>
                <Route path={ROUTES.ABOUT} component={AboutPage} />
            </Switch>
        </MainLayout>
    )
}